import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

df_train = r'training_generated_sensor_data.cvs'


df_train = pd.read_csv(df_train)

#feature target
X = df_train[["temperature", "humidity", "sound"]]
y = df_train["anomaly"]   

#Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42 #the same joke again...
)

#Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

#Evaluate
y_pred = model.predict(X_test)

print("\nCLASSIFICATION REPORT:\n")
print(classification_report(y_test, y_pred))

#Save model
joblib.dump(model, "anomaly_model.pkl")
print("Model saved successfully")