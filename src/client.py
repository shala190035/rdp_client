from datetime import datetime
import pandas as pd
import requests

def read_csv(filepath):
    # CSV einlesen
    df = pd.read_csv(filepath)
    return df

def send_temp_data_to_api(data, api_url):
    headers = {'Content-Type': 'application/json'}
    for c in range(len(data)):
        payload = {
            "value_time": int(datetime.fromisoformat(data["time"].iloc[c]).timestamp()),
            "value_type_id": 1,  # temperature type id
            "value": data["tl_i"].iloc[c],
            "device_id": 1  
        }
        res = requests.post(api_url, json=payload, headers=headers)
        print(res.status_code, res.json())  # Printing response

"""
def send_hum_data_to_api(data, api_url):
    headers = {'Content-Type': 'application/json'}
    for c in range(len(data)):
        payload = {
            "value_time": int(datetime.fromisoformat(data["time"].iloc[c]).timestamp()),
            "value_type_id": 1,
            "value": data["rfb_i"].iloc[c],
            "device_id": 1
        }
        res = requests.post(api_url, json=payload, headers=headers)
        print(res.status_code, res.json())  # Printing each response to debug
"""

if __name__ == "__main__":
    filepath = input("Geben Sie den Pfad zur CSV-Datei an: ")
    data = read_csv(filepath)

    # API-URL
    api_url = 'http://localhost:8000/api/value/'
    send_temp_data_to_api(data, api_url)
    #send_hum_data_to_api(data, api_url)