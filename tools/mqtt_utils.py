import os
import paho.mqtt.client as mqtt
from dotenv import load_dotenv

load_dotenv()

def create_client(on_connect=None, on_message=None, client_id=None):
    client = mqtt.Client(
        client_id=client_id,
        protocol=mqtt.MQTTv5,

    )
    client.username_pw_set(os.getenv("MQTT_USERNAME"), os.getenv("MQTT_PASSWORD"))
    if on_connect:
        client.on_connect = on_connect
    if on_message:
        client.on_message = on_message
    return client
