// C++ code
//

int sensorValue = 0;

void setup()
{
  Serial.begin(9600);
  pinMode(2, INPUT);
}

void loop()
{
  sensorValue = analogRead(A0);
  
  Serial.print("Sensor Value: ");
  Serial.print(sensorValue);
  
}