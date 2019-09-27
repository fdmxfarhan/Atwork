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
}

void loop() {
  int right = srf(2);
  int left = srf(3);
  int front = srf(4);
  
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
  
//  delay(10);
}
