const int BUZZ = 13;
const int SENSOR = 2;
int valor;
void setup() {
  pinMode(BUZZ, OUTPUT);
  pinMode(SENSOR, INPUT);

}

void loop() {
  valor = digitalRead(SENSOR);
  digitalWrite(BUZZ, !valor); //si es high lo manda a low y viceversa
}
