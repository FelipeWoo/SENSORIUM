import uuid, time
from tools.mqtt_utils import create_client
import os

ping_topic = f"sensorium/ping/{uuid.uuid4()}"
ping_payload = "ping"
message_received = False

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("✅ Conectado a MQTT.")
        client.subscribe(ping_topic)
        client.publish(ping_topic, ping_payload)

def on_message(client, userdata, msg):
    global message_received
    if msg.topic == ping_topic and msg.payload.decode() == ping_payload:
        print("✅ Ping recibido correctamente.")
        message_received = True
        client.disconnect()

client = create_client(on_connect, on_message)
client.connect(os.getenv("MQTT_HOST"), int(os.getenv("MQTT_PORT")))
client.loop_start()

for _ in range(10):
    if message_received:
        break
    time.sleep(0.5)

client.loop_stop()
if not message_received:
    print("❌ No se recibió el ping de vuelta.")
