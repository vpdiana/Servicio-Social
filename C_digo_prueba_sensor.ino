const int BUZZ = 13;
const int SENSOR = 3;
int valor;
void setup() {
  pinMode(BUZZ, OUTPUT); //el buzzer manda un sonido a la salida
  pinMode(SENSOR, INPUT); //se interpreta la entrada del sensor (deteccion)

}

void loop() {
  valor = digitalRead(SENSOR);
  digitalWrite(BUZZ, !valor); // se niega el valor para que el buzzer suene al detectar movimiento
}
