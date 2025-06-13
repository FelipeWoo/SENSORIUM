from controller.com import CommInterface

class DAQ:
    def __init__(self, comm: CommInterface):
        self.comm = comm
        self.subscribed = []
    
    def subscribe(self, sensor_id):
        self.subscribed.append(sensor_id)

    def read_all(self):
        return {id: self.comm.receive(id) for id in self.subscribed}