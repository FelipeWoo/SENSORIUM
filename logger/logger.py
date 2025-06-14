from tools.db_utils import get_db_connection, create_logs_table, insert_log
from tools.mqtt_utils import create_client
import json
import os
# Inicializar base de datos
DB_CONN = get_db_connection()
create_logs_table(DB_CONN)

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        
        insert_log(DB_CONN, data["sensor"], data["value"])
        print(f"Logged {data}")
    except Exception as e:
        print("Error al procesar mensaje MQTT:", e)

def main():
    client = create_client(on_message=on_message)
    try:
        client.connect(os.getenv("MQTT_HOST"), int(os.getenv("MQTT_PORT")))
        client.subscribe("sensor/temp1")
        print("📡 Escuchando en sensor/temp1 ...")
        
        client.loop_forever()
    except Exception as e:
        print("Error al conectar con MQTT:", e)

if __name__ == "__main__":
    main()
