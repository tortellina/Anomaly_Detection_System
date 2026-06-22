import requests

#normal check
data = {
    "temperature": 30,
    "humidity": 50,
    "sound": 40
}

res = requests.post("http://127.0.0.1:5000/predict", json=data)
print(res.json())

#anomaly check
data = {
    "temperature": 41,
    "humidity": 73,
    "sound": 82
}

res = requests.post("http://127.0.0.1:5000/predict", json=data)
print(res.json())

#void input
data = {}
res = requests.post("http://127.0.0.1:5000/predict", json=data)
print(res.json())

#missing values
data = {"temperature": 30}
res = requests.post("http://127.0.0.1:5000/predict", json=data)
print(res.json())

#not accepted types of values
data = {"temperature": "hot", "humidity": True, "sound": 50}
res = requests.post("http://127.0.0.1:5000/predict", json=data)
print(res.json())