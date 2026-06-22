from flask import Flask, request, jsonify
import pandas as pd
import joblib
import os
from datetime import datetime

app = Flask(__name__)
model = joblib.load("anomaly_model.pkl")

REQUIRED_FEATURES = ["temperature", "humidity", "sound"]

def log_prediction(data, prediction):

    log_entry = pd.DataFrame([{
        "timestamp": datetime.now(),
        "temperature": data["temperature"],
        "humidity": data["humidity"],
        "sound": data["sound"],
        "prediction": "ANOMALY" if prediction == 1 else "NORMAL"
    }])

    file_name = "prediction_log.csv"

    if os.path.exists(file_name):
        log_entry.to_csv(
            file_name,
            mode="a",
            header=False,
            index=False
        )
    else:
        log_entry.to_csv(
            file_name,
            index=False
        )

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    
    # Check JSON exists
    if data is None:
        return jsonify({"error": "Invalid JSON body"}), 400

    #Check required fields
    missing = [f for f in REQUIRED_FEATURES if f not in data]
    if missing:
        return jsonify({
            "error": "Missing features",
            "missing": missing
        }), 400


    # Validate types (must be numeric)

    try:
        features = pd.DataFrame([{
            "temperature": float(data["temperature"]),
            "humidity": float(data["humidity"]),
            "sound": float(data["sound"])
        }])
    except (ValueError, TypeError):
        return jsonify({
            "error": "All features must be numeric"
        }), 400


    # Predict safely
    try:
        prediction = model.predict(features)[0]
        log_prediction(data, prediction)
    except Exception as e:
        return jsonify({
            "error": "Model prediction failed",
            "details": str(e)
        }), 500


    # Return structured response
    return jsonify({
        "anomaly": int(prediction),
        "status": "anomaly" if prediction == 1 else "normal"
    })

@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True)