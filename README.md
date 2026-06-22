# Anomaly Detection System with Stream Processing

## Introduction

This project presents an end-to-end anomaly detection system designed for wind turbine monitoring, demonstrating how a machine learning model can be transformed into a production-ready service.

The system detects anomalies in sensor (temperature, humidity, and sound) using a supervised machine learning approach. It is deployed as a Flask-based REST API and enhanced with a stream processing simulation layer to emulate real-time IoT environments.

The system simulates continuous data flow, processes incoming sensor readings in real time and returns predictions through a structured API response. This allows the project to closely replicate real-world industrial monitoring scenarios.

---

## Features

The system is built around several key components that work together to enable real-time anomaly detection. At its core is a supervised machine learning model based on a Random Forest Classifier, which is trained to distinguish between normal and anomalous turbine behavior using sensor data. This model is deployed through a Flask REST API, which exposes a /predict endpoint for real-time inference and a /health endpoint for system monitoring and availability checks.

To replicate a realistic industrial environment, a stream processing simulation layer is included. This component generates synthetic IoT sensor data and sends it to the API as sequential HTTP requests with controlled delays, effectively mimicking real-time data streaming from distributed sensors.

The system also includes a robust data pipeline responsible for ensuring reliable operation. Incoming requests are validated through strict schema enforcement, preprocessed into a model-compatible format, and protected with error-handling mechanisms to maintain system stability even when unexpected inputs occur.

In addition, a logging system records every prediction made by the model. Each log entry includes a timestamp, the input sensor values, and the corresponding prediction output, all stored in a CSV file. This ensures full traceability and supports future analysis or model retraining.

Finally, the trained model is persisted using Joblib and loaded once at application startup. This design choice improves efficiency by avoiding repeated model loading and ensures fast, low-latency predictions during runtime.


The system follows a full model-to-production pipeline:

    Data Generation → Training → Deployment → Stream Processing → Prediction → Logging


## Installation

download the repository and create a virtual  enviroment:
python -m venv venv
venv\Scripts\activate

install the required libraries and dependencies:
pip install -r requirements.txt


## RUN THE SYSTEM
 STEP 1: GENERATE THE DATASETS
    py generate_data.py

STEP 2: VISUALIZE THE DATASETS DISTRIBUITIONS (OPTIONAL)
    py datasets_visualization.py

STEP 3: TRAIN THE MODEL
    python train_model.py

STEP 4: START THE API SERVER
    python app.py

STEP 5: RUN STREAM SIMULATION (OPEN ANOTHER TERMINAL)
    py stream_simulation.py


## Conclusion

This system demonstrates a complete anomaly detection pipeline, transforming a machine learning model into a real-time, production-style microservice. 
It highlights key principles of modern ML engineering, including stream processing, API deployment, logging, and system monitoring.


## authors
student name: Vittoria Tagliabue (9212846)
course name: Project: From Model to Production
course code DLBDSMTP01 
tutor: Anna Androvitsanea
