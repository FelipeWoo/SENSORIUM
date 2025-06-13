
import time, uuid
from math import sin, pi

from sensors.sensors import TemperatureSensor
from controller.daq import DAQ
from controller.com import CAN


# First order transfer function
def tf_first_order(u): return 0.8 * u

# Variable input signal
def input_signal(t): return 5 + 2*sin(2*pi*0.1*t)

# CAN comm
can_com = CAN()

# Sensor
temp_sensor = TemperatureSensor(
    id=uuid.uuid4(),
    name="mcu_temp", 
    input_fn=input_signal,
    transfer_fn=tf_first_order,
    unit="°C", 
    comm=can_com
    )

# DAQ
daq = DAQ(can_com)
daq.subscribe("mcu_temp")


def main():
     # Simulation Loop
     t = 0

     while True:
          temp_sensor.update(t)
          print(daq.read_all())
          time.sleep(1)
          t+=1


if __name__ == "__main__":
    main()
