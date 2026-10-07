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
- GPIO: Genereal Purpose Input / Output
- High Potential Energy
- Lower Potential Energy
- MQTT
- Pin
- Resistance (Ohms)
- Real Time Clock (RTC)
- Relay Module
- Sensors
- Transducers
- Voltage (Volts, V)
- VCC

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
- 5v Relay Module (Active Low)
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

- Flipped connected pins between transmitter and probe, observed

Sensor in air -> 1023
Sensor in dry soil -> 950 - 850
Sensor in wet soil -> 150 - 200

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

## Pump

- Connected Relay module
  - 5V micro controller to VCC
  - GND micro controller to GND
  - GPIO to IN (RELAY)
- Connected Pump to Relay Module and battery holder
  - PUMP (+) to relay NO
  - Battery (+) to Relay CMD
  - Pump (-) to Battery (-)
- Tried Connecting a switch for manually controlling the pump for testing

```txt
              Microcontroller
              ┌──────────────┐
       5V ────┤ Relay VCC    │
      GND ────┤ Relay GND    │
     GPIO ────┤ Relay IN     │
              └──────────────┘

        Moisture Sensor
       VCC ───── 5V
       GND ───── GND
       OUT ───── GPIO


          5V Pump Supply
          + ───── COM
                    │
                    NO ───── Pump +
          - ──────────────── Pump -
```

**Observations:**

- Relay Stays ON when LOW signal is passed and OFF when HIGH signal is passed
- PUMP comes ON when RELAY is powered OFF and vice versa
- Connected switch is on stable with both normal and pull down connection
