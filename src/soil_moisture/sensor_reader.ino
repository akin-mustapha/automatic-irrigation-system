// C++ code
//

int sensorValue = 0;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  sensorValue = analogRead(A0);
  // Send formatted data over Serial every 5 seconds
  Serial.print("Sensor Value: ");
  Serial.println(sensorValue);

  delay(5000);
}