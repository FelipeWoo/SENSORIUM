from controller.comm import CommInterface
import time, json

class DAQ:
    def __init__(self, input_comm, output_comm):
        self.input_comm = input_comm    # CAN
        self.output_comm = output_comm  # MQTT
        self.subscribed = []
    
    def subscribe(self, sensor_id, metadata=None):
        self.subscribed.append((sensor_id, metadata or {}))

    def read_all(self, t=None):
        for sensor_id, metadata in self.subscribed:

            value = self.input_comm.receive(sensor_id)

            name = metadata.get("name", sensor_id)
            payload = {
                "timestamp": time.time(),
                "id": str(sensor_id),
                "name": name,
                "value": value,
                "unit": metadata.get("unit", "")
            }
            self.output_comm.send(name, payload)