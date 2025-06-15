# SENSORIUM

SENSORIUM is a modular Python simulation framework for industrial sensor systems, communication protocols, and data acquisition workflows.

This repository represents a prototype environment for simulating and testing sensors over a virtual CAN bus, with downstream publishing via MQTT and a listener system for processing and visualization.

The project is currently in progress but functional enough to demonstrate end-to-end simulation.

---

## Project Status

This is a working prototype. The simulation framework is operational and includes:

- Configurable sensors with transfer functions
- CAN-based communication simulation
- MQTT message publication
- Listener that decodes and prints structured payloads

The system is intentionally modular for future integration with real hardware, cloud pipelines, or dashboards.

---

## Architecture Overview

```
    Sensor (virtual) → CAN bus (simulated) → DAQ (simulated)→ MQTT Broker → Listener
```

- Sensors simulate analog input and apply a transfer function.
- The DAQ subscribes to sensor IDs, reads from the CAN bus, adds metadata, and publishes the output via MQTT.
- The listener consumes MQTT messages and displays or processes them.

---

## Features

- Sensor definitions with realistic signal simulation
- Faulty sensor logic for dropout and failure handling
- Clean separation of communication interfaces (`CAN`, `MQTT`)
- Central DAQ for multi-sensor acquisition and data forwarding
- Dynamic publishing to shared MQTT topics with structured JSON payloads

---

## Technologies Used

- Python 3.12
- `paho-mqtt` for MQTT communication
- `uuid` for unique device IDs
- `dotenv` for environment configuration
- Simple modular design: no external frameworks required

---

## Usage

### Prerequisites

- Python 3.12+
- Local MQTT broker (e.g. Mosquitto on port 1883)
- `uv` environment or `venv` + `pip`

### Running the Simulation

```bash
uv pip install -r requirements.txt

uv run -m main                # Starts the sensor simulation and DAQ
uv run -m controller.listener # Starts the MQTT listener
````

Or use plain `python` if you're not using `uv`.

---

## Future Development Plans


* Real-time visualization via terminal UI or web-based dashboard
* Grafana integration for time series data monitoring
* Expanded sensor catalog and transfer function modeling
* Simulation of latency, noise, dropouts, and protocol failures
* Dockerized deployment for distributed and reproducible environments
* Implementation of a Go-based controller
* Addition of Python-based actuator simulation
---

