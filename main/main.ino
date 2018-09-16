const int ledPin = 13;      // LED connected to digital pin 13
const int buzzPin = 12;
const int knockSensor0 = A0; // the piezo is connected to analog pin 0
const int knockSensor1 = A1;
const int knockSensor2 = A2;
const int knockSensor3 = A3;
const int threshold = 200;  // threshold value to decide when the detected sound is a knock or not


// these variables will change:
int sensorReading0 = 0;
int sensorReading1 = 0;
int sensorReading2 = 0;
int sensorReading3 = 0;
int ledState = LOW;         // variable used to store the last LED status, to toggle the light
int buzzState = LOW;

void trigger()
{
    Serial.println(1);
    for(int i = 0;i<9;i++){
      
      ledState=!ledState;
      digitalWrite(ledPin, ledState);
      buzzState=!buzzState;
      digitalWrite(buzzPin,HIGH);
      delay(100);
    }
}

void setup() {
  pinMode(ledPin, OUTPUT); // declare the ledPin as as OUTPUT
  pinMode(buzzPin, OUTPUT);
  Serial.begin(9600);       // use the serial port
}

void loop() {
  // read the sensor and store it in the variable sensorReading:
  sensorReading0 = analogRead(knockSensor0);
  sensorReading1 = analogRead(knockSensor1);
  sensorReading2 = analogRead(knockSensor2);
  sensorReading3 = analogRead(knockSensor3);
  bool fall = (sensorReading0 < 200) && (sensorReading1 < 200) && (sensorReading2 < 200) &&(sensorReading3 < 200); 
  if(fall)
  {  
    trigger();
  }
  Serial.print(sensorReading0);
  Serial.print(" ");
  Serial.print(sensorReading1);
  Serial.print(" ");
  Serial.print(sensorReading2);
  Serial.print(" ");
  Serial.println(sensorReading3);
  delay(100);  //   delay to avoid overloading the serial port buffer
}
