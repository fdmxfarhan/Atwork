#include <Arduino.h>
#include <Wire.h>
#include <HMC5883L_Simple.h>

HMC5883L_Simple Compass;
int distance=0;

int srf(int pin){
  pinMode(pin,OUTPUT);
  digitalWrite(pin,1);
  delayMicroseconds(10);
  digitalWrite(pin,0);
  pinMode(pin,INPUT);
  return(pulseIn(pin, 1)*0.034/2);
}

void setup() {
  Serial.begin(9600);
  pinMode(12, INPUT);
  Wire.begin();
  Compass.SetDeclination(23, 35, 'E');  
  Compass.SetSamplingMode(COMPASS_SINGLE);
  Compass.SetScale(COMPASS_SCALE_130);
  Compass.SetOrientation(COMPASS_HORIZONTAL_X_NORTH);
}

void loop() {
  int right = srf(2);
  int left = srf(3);
  int front = srf(4);
  float heading = Compass.GetHeadingDegrees();
  int angle = heading * 255/360;
  if(digitalRead(12) == 1) Serial.write('A');
  
  Serial.write("R");
  Serial.write((right/100)%10+'0');
  Serial.write((right/10)%10+'0');
  Serial.write((right/1)%10+'0');
  Serial.write("L");
  Serial.write((left/100)%10+'0');
  Serial.write((left/10)%10+'0');
  Serial.write((left/1)%10+'0');
  Serial.write("F");
  Serial.write((front/100)%10+'0');
  Serial.write((front/10)%10+'0');
  Serial.write((front/1)%10+'0');
  Serial.write("C");
  Serial.write((angle/100)%10+'0');
  Serial.write((angle/10)%10+'0');
  Serial.write((angle/1)%10+'0');
//  delay(100);
}
