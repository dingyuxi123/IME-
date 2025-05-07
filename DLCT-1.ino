#define p1 3
#define p2 4
#define p3 5
#define p4 6

void charge(void);
float offset(void);
float ref(void);
float sense(void);

void setup() {
  Serial.begin(9600);
}

void loop() {

  charge();
  float off = offset();

  charge();
  float reference = ref();

  charge();
  float snse = sense();
 float y=(snse-off)/(reference-off);

  // Serial.print("Offset: ");
  // Serial.print(off);
  // Serial.print(" us, Ref: ");
  // Serial.print(reference);
  // Serial.print(" us, Sense: ");
  // Serial.print(snse);

  // Serial.print(" us ");
    Serial.println(y);
 
delay(100);
}

void charge() {
  pinMode(p1, OUTPUT);
  digitalWrite(p1, HIGH);
  delay(1);
  pinMode(p1, INPUT);
}

float offset() {
  pinMode(p2, OUTPUT);
  digitalWrite(p2, LOW);
  pinMode(p1, INPUT);

  unsigned long t = micros();
  while (digitalRead(p1) == HIGH);
  unsigned long t1 = micros();

  pinMode(p2, INPUT);
  return (float)(t1 - t);
}

float ref() {
  pinMode(p4, OUTPUT);
  digitalWrite(p4, LOW);

  unsigned long t = micros();
  while (digitalRead(p1) == HIGH);
    unsigned long t1 = micros();

  pinMode(p4, INPUT);
  return (float)(t1 - t);
}

float sense() {
  pinMode(p3, OUTPUT);
  pinMode(p4, OUTPUT);
  digitalWrite(p3, LOW);
  digitalWrite(p4, LOW);  
  unsigned long t = micros();
  while (digitalRead(p1) == HIGH);
  unsigned long t1 = micros();

  pinMode(p3, INPUT);
  pinMode(p4, INPUT);
  return (float)(t1 - t);
}
