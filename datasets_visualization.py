import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_train = r'training_generated_sensor_data.cvs'
df_stream = r'stream_generated_sensor_data.cvs'

def train_dataset_visualization(df_train):
    #visualization of training data 
    df_train = pd.read_csv(df_train)
    print(df_train.shape)

    #histograms of temperature, humidity and sound distribuitions
    df_train[["temperature", "humidity", "sound"]].hist(bins=30, figsize=(10,5))
    plt.show()

    normal = df_train[df_train["anomaly"] == 0]
    anomaly = df_train[df_train["anomaly"] == 1]

    #histogram of temperature anomaly\normal comparison
    plt.figure(figsize=(10,5))
    plt.hist(normal["temperature"], bins=30, alpha=0.6, label="Normal")
    plt.hist(anomaly["temperature"], bins=30, alpha=0.6, label="Anomaly")
    plt.title("train Temperature Distribution: Normal vs Anomaly")
    plt.legend()
    plt.show()

    #histogram of humidity anomaly\normal comparison
    plt.figure(figsize=(10,5))
    plt.hist(normal["humidity"], bins=30, alpha=0.6, label="Normal")
    plt.hist(anomaly["humidity"], bins=30, alpha=0.6, label="Anomaly")
    plt.title("train humidity Distribution: Normal vs Anomaly")
    plt.legend()
    plt.show()

    #histogram of sound anomaly\normal comparison
    plt.figure(figsize=(10,5))
    plt.hist(normal["sound"], bins=30, alpha=0.6, label="Normal")
    plt.hist(anomaly["sound"], bins=30, alpha=0.6, label="Anomaly")
    plt.title("train sound Distribution: Normal vs Anomaly")
    plt.legend()
    plt.show()

def stream_dataset_visualization(df_stream):
    #visualization of training data 
    df_stream = pd.read_csv(df_stream)
    print(df_stream.shape)
    normal = df_stream[df_stream["anomaly"] == 0]
    anomaly = df_stream[df_stream["anomaly"] == 1]

    #histograms of temperature, humidity and sound distribuitions
    df_stream[["temperature", "humidity", "sound"]].hist(bins=30, figsize=(10,5))
    plt.show()

    #histogram of temperature anomaly\normal comparison
    plt.figure(figsize=(10,5))
    plt.hist(normal["temperature"], bins=30, alpha=0.6, label="Normal")
    plt.hist(anomaly["temperature"], bins=30, alpha=0.6, label="Anomaly")
    plt.title("stream Temperature Distribution: Normal vs Anomaly")
    plt.legend()
    plt.show()


    #histogram of humidity anomaly\normal comparison
    plt.figure(figsize=(10,5))
    plt.hist(normal["humidity"], bins=30, alpha=0.6, label="Normal")
    plt.hist(anomaly["humidity"], bins=30, alpha=0.6, label="Anomaly")
    plt.title("stream humidity Distribution: Normal vs Anomaly")
    plt.legend()
    plt.show()


    #histogram of sound anomaly\normal comparison
    plt.figure(figsize=(10,5))
    plt.hist(normal["sound"], bins=30, alpha=0.6, label="Normal")
    plt.hist(anomaly["sound"], bins=30, alpha=0.6, label="Anomaly")
    plt.title("stream sound Distribution: Normal vs Anomaly")
    plt.legend()
    plt.show()

train_dataset_visualization(df_train)
stream_dataset_visualization(df_stream)


