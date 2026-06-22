import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42) #I read it is for the joke, so here is 42
N_SAMPLES = 10000
ANOMALY_RATE = 0.05

# def generate_normal():
#     return {
#         "temperature": np.random.normal(25, 3),
#         "humidity": np.random.normal(50, 10),
#         "sound": np.random.normal(40, 5),
#         "anomaly": 0
#     }

# def generate_anomaly():
#     return {
#         "temperature": np.random.normal(80, 10),
#         "humidity": np.random.normal(15, 5),
#         "sound": np.random.normal(100, 15),
#         "anomaly": 1
#     }

def generate_normal():
    return {
        "temperature": np.random.normal(30, 8),
        "humidity": np.random.normal(45, 12),
        "sound": np.random.normal(50, 10),
        "anomaly": 0
    }

def generate_anomaly():
    return {
        "temperature": np.random.normal(45, 12),
        "humidity": np.random.normal(30, 15),
        "sound": np.random.normal(70, 20),
        "anomaly": 1
    }

def create_dataset(N_SAMPLES, ANOMALY_RATE):
    data = []

    for _ in range(N_SAMPLES):
        if np.random.rand() < ANOMALY_RATE:
            data.append(generate_anomaly())
        else:
            data.append(generate_normal())

    return pd.DataFrame(data)

df_train = create_dataset(N_SAMPLES, ANOMALY_RATE)
df_train.to_csv("training_generated_sensor_data.cvs", index=False)

df_stream = create_dataset(N_SAMPLES, ANOMALY_RATE)
df_train.to_csv('stream_generated_sensor_data.cvs', index= False)

print("\n===== BASIC df_train DATASET STATS =====\n")
print("Shape:", df_train.shape)
print("\nMissing values:\n", df_train.isnull().sum())
print("\nNumerical summary:\n", df_train.describe())
if "anomaly" in df_train.columns:
    print("\nAnomaly distribution:")
    print(df_train["anomaly"].value_counts())
    print("\nAnomaly rate:", df_train["anomaly"].mean())
print('\nDISPLAY OF FIRST df_train 10 ROWS:\n', df_train.head(10))



print("\n===== BASIC df_stream DATASET STATS =====\n")
print("Shape:", df_stream.shape)
print("\nMissing values:\n", df_stream.isnull().sum())
print("\nNumerical summary:\n", df_stream.describe())
if "anomaly" in df_stream.columns:
    print("\nAnomaly distribution:")
    print(df_stream["anomaly"].value_counts())
    print("\nAnomaly rate:", df_stream["anomaly"].mean())
print('\nDISPLAY OF FIRST df_stream 10 ROWS:\n', df_stream.head(10))


