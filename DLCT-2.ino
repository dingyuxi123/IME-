#define p1 3
#define p2 4
#define p3 5
#define p4 6
#define p5 7
void charge(void);
float offset(void);
float ref(void);
float sense(void);

void setup() {
  Serial.begin(9600);
}

void loop() {
    float sum=0;
     for(int i=0;i<20;i++){
  charge();
  float off = offset();

  charge();
  float reference1 = ref1();

  charge();
  float snse1 = sense1();
  
  charge();
  float reference2 = ref2();

  charge();
  float snse2 = sense2();
  float y=(snse1-off)/(reference1-off)+(snse2-off)/(reference2-off);
 sum=sum+y;
   // Serial.print("Offset: ");
  // Serial.print(off);
  // Serial.print(" us, Ref1: ");
  // Serial.print(reference1);
  // Serial.print(" us, Sense1: ");
  // Serial.print(snse1);
  // Serial.print(" us, Ref2: ");
  // Serial.print(reference2);
  // Serial.print(" us, Sense2: ");
  // Serial.print(snse2);
  // Serial.print(" us");
     }
     sum=sum/20;

  Serial.println(sum);
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
  while (digitalRead(p1) == HIGH){if((micros()-t)>100000){Serial.println("off");
  return;}}
  unsigned long t1 = micros();

  pinMode(p2, INPUT);
  return (float)(t1 - t);
}

float ref1() {
  pinMode(p4, OUTPUT);
  digitalWrite(p4, LOW);
  unsigned long t = micros();
  while (digitalRead(p1) == HIGH){if((micros()-t)>100000){Serial.println("ref1");
  return;}}  unsigned long t1 = micros();
  pinMode(p4, INPUT);
  return (float)(t1 - t);
}
float ref2() {
  pinMode(p5, OUTPUT);
  digitalWrite(p5, LOW);
  unsigned long t = micros();
  while (digitalRead(p1) == HIGH){if((micros()-t)>100000){Serial.println("ref2");
  return;}}  unsigned long t1 = micros();
  pinMode(p5, INPUT);
  return (float)(t1 - t);
}

float sense1() {
  pinMode(p3, OUTPUT);
  pinMode(p4, OUTPUT);
  digitalWrite(p3, LOW);
  digitalWrite(p4, LOW);  
  unsigned long t = micros();
  while (digitalRead(p1) == HIGH){if((micros()-t)>100000){Serial.println("sen1");
  return;}}  unsigned long t1 = micros();

  pinMode(p3, INPUT);
  pinMode(p4, INPUT);
  return (float)(t1 - t);
}
float sense2() {
  pinMode(p3, OUTPUT);
  pinMode(p5, OUTPUT);
  digitalWrite(p3, LOW);
  digitalWrite(p5, LOW);  
  unsigned long t = micros();
  while (digitalRead(p1) == HIGH){if((micros()-t)>100000){Serial.println("sen2");
  return;}}  unsigned long t1 = micros();

  pinMode(p3, INPUT);
  pinMode(p5, INPUT);
  return (float)(t1 - t);
}
