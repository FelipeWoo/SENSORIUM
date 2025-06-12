import os
import time
import random
import paho.mqtt.client as mqtt
from dotenv import load_dotenv

load_dotenv()

MQTT_HOST = os.getenv("MQTT_HOST", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_USER = os.getenv("MQTT_USERNAME")
MQTT_PASS = os.getenv("MQTT_PASSWORD")

client = mqtt.Client()
client.username_pw_set(MQTT_USER, MQTT_PASS)
client.connect(MQTT_HOST, MQTT_PORT)

while True:
    value = round(random.uniform(20, 30), 2)
    payload = f'{{"sensor": "temp1", "value": {value}}}'
    client.publish("sensor/temp1", payload)
    print("📡 Published:", payload)
    time.sleep(2)
