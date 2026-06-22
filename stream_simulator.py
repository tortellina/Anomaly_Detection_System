import requests
import time
import numpy as np
import pandas as pd
import random
from datetime import datetime


# =========================
# CONFIGURATION
# =========================

API_URL = "http://127.0.0.1:5000/predict"
SLEEP_TIME = 1  # seconds between requests
CSV_PATH = "stream_generated_sensor_data.cvs"


# =========================
# LOAD DATA
# =========================

df_stream = pd.read_csv(CSV_PATH)
df_stream  = df_stream.drop(columns=['anomaly'])

print(f"Loaded dataset with {len(df_stream)} rows")

# =========================
# STREAM SIMULATION
# =========================

print("\nStarting CSV stream simulation...\n")

for i, row in df_stream.iterrows():

    data = {
        "temperature": float(row["temperature"]),
        "humidity": float(row["humidity"]),
        "sound": float(row["sound"])
    }

    try:
        response = requests.post(API_URL, json=data, timeout=2)
        result = response.json()

        timestamp = datetime.now().strftime("%H:%M:%S")

        status = "NORMAL"
        if result.get("anomaly") == 1:
            status = "ANOMALY"

        print(f"[{timestamp}] Row {i} → {data} → {status}")

    except requests.exceptions.RequestException as e:
        print(f"API error at row {i}:", e)

    time.sleep(SLEEP_TIME)

