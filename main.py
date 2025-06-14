import random, time, uuid
from math import sin, pi

from sensors.sensors import TemperatureSensor
from controller.daq import DAQ
from controller.comm import CAN, MQTT


# First order transfer function
def tf_first_order(u): return 0.8 * u


def tf_with_noise_and_delay(u, delay=0.2):
    noise = random.gauss(0, 0.05)  # Gaussian Noise
    return 0.8 * (u - delay) + noise

# Variable input signal
def input_signal(t): return 5 + 2*sin(2*pi*0.1*t)



# Comms
can_comm = CAN()
mqtt_comm = MQTT("sensorium/data")

# Sensor
temp_sensor = TemperatureSensor(
    id=uuid.uuid4(),
    name="mcu_temp", 
    input_fn=input_signal,
    transfer_fn=tf_first_order,
    unit="°C", 
    comm=can_comm
    )

temp_sensor_noise = TemperatureSensor(
    id=uuid.uuid4(),
    name="mcu_temp_noise", 
    input_fn=input_signal,
    transfer_fn=tf_with_noise_and_delay,
    unit="°C", 
    comm=can_comm
    )

# DAQ
daq = DAQ(can_comm, mqtt_comm)

daq.subscribe(temp_sensor.id, metadata={
    "name": temp_sensor.name,
    "unit": temp_sensor.unit
})

daq.subscribe(temp_sensor_noise.id, metadata={
    "name": temp_sensor_noise.name,
    "unit": temp_sensor_noise.unit
})



def main():
    # Simulation Loop
    t = 0
    print(f"Sending messages (Press Ctrl+C to stop)")
    try:
        while True:
            temp_sensor.update(t)
            temp_sensor_noise.update(t)
            daq.read_all(t)
            time.sleep(5)
            t+=1
    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")

if __name__ == "__main__":
    main()
