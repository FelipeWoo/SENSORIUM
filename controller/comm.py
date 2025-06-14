import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os
import json, time

load_dotenv()

MQTT_HOST = os.getenv("MQTT_HOST", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_USER = os.getenv("MQTT_USERNAME")
MQTT_PASS = os.getenv("MQTT_PASSWORD")


# === Base Interface ===
class CommInterface:
    def send(self, name, value):
        raise NotImplementedError

    def receive(self, name):
        raise NotImplementedError


# === CAN Simulation ===
class CAN(CommInterface):
    def __init__(self):
        self.bus = {}

    def send(self, name, value):
        self.bus[name] = value

    def receive(self, name):
        return self.bus.get(name, None)


# === MQTT Communication ===
class MQTT(CommInterface):
    def __init__(self, topic_prefix):
        self.client = mqtt.Client()
        if MQTT_USER and MQTT_PASS:
            self.client.username_pw_set(MQTT_USER, MQTT_PASS)

        self.client.connect(MQTT_HOST, MQTT_PORT)
        self.topic_prefix = topic_prefix

    def send(self, name, payload):
        topic = f"{self.topic_prefix}/{name}"

        # Ensure it's only encoded once
        if isinstance(payload, dict):
            payload = json.dumps(payload)
        elif not isinstance(payload, str):
            raise TypeError("Payload must be dict or JSON string.")

        self.client.publish(topic, payload)

    def receive(self, name):
        pass  # Not implemented for now
