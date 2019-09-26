void setup() {
  Serial.begin(9600);
}

void loop() {
  char a = Serial.read();
  if(a != -1)  Serial.print(a);
}
