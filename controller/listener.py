import paho.mqtt.client as mqtt
import json
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

MQTT_HOST = os.getenv("MQTT_HOST", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_USER = os.getenv("MQTT_USERNAME")
MQTT_PASS = os.getenv("MQTT_PASSWORD")
TOPIC = "sensorium/data/#"

# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with result code {rc}")
    client.subscribe(TOPIC)

# Callback when a message is received
def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        data = json.loads(payload)

        topic = msg.topic
        sensor_id = data.get("id", "unknown")
        value = data.get("value", "n/a")
        unit = data.get("unit", "")
        timestamp = data.get("timestamp", "n/a")

        print(f"Topic: {topic} → {sensor_id}: {value} {unit} @ {timestamp}")
    except Exception as e:
        print(f"Error decoding message: {e}")


def main():
    client = mqtt.Client()

    if MQTT_USER and MQTT_PASS:
        client.username_pw_set(MQTT_USER, MQTT_PASS)

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_HOST, MQTT_PORT, keepalive=60)

    print(f"Listening to topic: {TOPIC} (Press Ctrl+C to stop)")
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("\nListener stopped by user.")

if __name__ == "__main__":
    main()
