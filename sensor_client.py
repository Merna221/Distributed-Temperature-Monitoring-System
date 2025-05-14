# sensor_client.py
import requests
import time
import random
import sys

sensor_id = sys.argv[1] if len(sys.argv) > 1 else "Sensor1"
url = "http://127.0.0.1:5000/add"

while True:
    temp = round(random.uniform(20, 40), 2)
    try:
        res = requests.post(url, json={'sensor_id': sensor_id, 'value': temp})
        print(f"📤 Sent: {temp}°C | Response: {res.json()}")
    except Exception as e:
        print(f"❌ Error sending data: {e}")
    time.sleep(3)
