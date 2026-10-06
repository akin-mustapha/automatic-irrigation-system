# Automatic Irrigation System

**Overview:** An automated system for watering house plant, this projects aims to build a system that collects soil moisture data at schedule and trigger watering process autonomusly.

## Glossary

- Actuators
- AC (50/60 time a sec)
- Baud Rate
- Bare electrode Probe
- Broker
- Circuits
- Client Certificate
- Current (Amperes, amps, A)
- DC
- Electricity
- High Potential Energy
- Lower Potential Energy
- MQTT
- Resistance (Ohms)
- Real Time Clock (RTC)
- Sensors
- Transducers
- Voltage (Volts, V)

## Tech Stack

- TinkerCad
- Arduino IDE

## Setup

- Install python
- Create python virtual environment

```sh
cd automatic-irrigation-system

python3 -m venv venv

source ./venv/bin/activate

touch requirements.txt

pip3 install -r requirements.txt
```

## Components

- DC Water Pump
- 5v Relay Module
- Plastic Battery Holder (4 AA batteries)
- Soil Moisture Sensor
- 0.5m vinyl hose
- Two Dupont cables
- Transmitter module

## V1

- Get sensor readings
- Log sensor readings to database

**Project Log:**

- simulated soil moisture sensor `circuits` on `tinkercad`
- Connected physical components
  - Micro-controller - Arduino Uno
  - Breadboard
  - Soil moisture probe
  - Transmitter module
- Collect Measurement

**Observed Sensor Reading:**

Sensor in air -> 1023
Sensor in dry soil -> 950 - 850
Sensor in wet soil -> 250 - 300

```txt
       Probe
      ┌──────┐
      │      │
      └──┬───┘
         │ 2 wires
         ▼
 ┌───────────────────────┐
 │  Transmitter module   │
 │    VCC GND DO AO      │
 └───────────────────────┘


Sensor module       Arduino
────────────────────────────
VCC        ───────── 5V
GND        ───────── GND
AO         ───────── A0
DO         ───────── (not connected)
```
