// Corrected Arduino Sketch for Switch & Relay Control

const int RELAY_PIN  = 8;  // Relay control pin
const int SWITCH_PIN = 1;  // Manual switch pin
const int SENSOR_PIN = A0; // Sensor pin

// Non-blocking timer variables for Serial output
unsigned long previousMillis = 0;
const long interval = 5000; // 5000 ms = 5 seconds

// Logic definitions for Active-LOW Relay module
#define RELAY_ON  LOW
#define RELAY_OFF HIGH

void setup()
{
  // 1. Configure Relay Pin (Ensure relay is OFF at startup)
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, RELAY_OFF);

  // 2. Configure Switch with internal Pull-up resistor
  // Switch OPEN  => pin reads HIGH (Relay OFF)
  // Switch CLOSED (pressed) => pin connected to GND reads LOW (Relay ON)
  pinMode(SWITCH_PIN, INPUT_PULLUP);

  Serial.begin(9600);
}

void loop()
{
  // --- INSTANT SWITCH RESPONSE (Runs continuously without delay) ---
  int switchState = digitalRead(SWITCH_PIN);
  int sensorValue = analogRead(SENSOR_PIN);

  // Since we use INPUT_PULLUP: LOW means the switch is closed / turned ON
  // if (switchState == LOW) {
  //   // digitalWrite(RELAY_PIN, RELAY_ON);  // Turn relay ON (LOW signal)
  //   Serial.println("XXX");
  // } else if (switchState == HIGH) {
  //   // digitalWrite(RELAY_PIN, RELAY_OFF); // Turn relay OFF (HIGH signal)
  //   Serial.println("YYY");
  // }

  // --- PERIODIC SERIAL OUTPUT (Every 5 seconds without blocking) ---
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;

    int relayState = digitalRead(RELAY_PIN);

    Serial.println("-----------------------------------");
    Serial.print("Sensor Value (A0): ");
    Serial.println(sensorValue);
    Serial.print("Relay Pin State (Pin 2): ");
    Serial.println(relayState == RELAY_ON ? "ON (LOW)" : "OFF (HIGH)");
    Serial.print("Switch State (Pin 3): ");
    Serial.println(switchState == LOW ? "ON / CLOSED" : "OFF / OPEN");
  }
}