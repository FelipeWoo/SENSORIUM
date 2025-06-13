

class CommInterface:
    def send(self, name, value):
        raise NotImplementedError

    def receive(self, name):
        raise NotImplementedError
    

class CAN(CommInterface):
    def __init__(self):
        self.bus = {}

    def send(self, name, value):
        self.bus[name] = value

    def receive(self, name):
        return self.bus.get(name, None)


class MQTT(CommInterface):
    def __init__(self, client):
        self.client = client


    def send(self, name, value):
        """name = topic"""
        self.client.publish(f"sensors/{name}", value)

    def receive(self, name):
        pass

