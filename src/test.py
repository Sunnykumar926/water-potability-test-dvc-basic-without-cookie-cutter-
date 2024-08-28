import json
import requests

url = "https://water-potebility-prediction-basic-dvc-4.onrender.com/predict"

X_new = dict (
    ph = 4.668101687405915,
    Hardness = 193.68173547507868,
    Solids = 47580.99160333534,
    Chloramines = 7.166638935482532,
    Sulfate = 359.94857436696,
    Conductivity = 526.4241709223593,
    Organic_carbon = 13.894418518194527,
    Trihalomethanes = 66.68769478539706,
    Turbidity = 4.4358209095098
    )


X_new_json = json.dumps(X_new)

response = requests.post(url, data = X_new_json)

print("Response Text: ", response.text)
print("Status Code: ", response.status_code)
