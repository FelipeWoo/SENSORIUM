from controller.comm import CommInterface

class SensorBase:
    def __init__(self, id, name, input_fn, transfer_fn, unit, comm: CommInterface):
        self.id = id
        self.name = name
        self.input_fn = input_fn
        self.transfer_fn = transfer_fn
        self.unit = unit
        self.comm = comm
 

    def update(self, t):
        """Update the output based on, time(t) and input"""
        u = self.input_fn(t)
        y = self.transfer_fn(u)
        self.comm.send(self.id,y)
    
class FaultySensor(SensorBase):
    def update(self, t):
        if 20 < t < 40:  # Temp Failure
            self.comm.send(self.id, None)
        else:
            super().update(t)

class TemperatureSensor(SensorBase):
    pass