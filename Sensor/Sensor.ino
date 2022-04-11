#include "DHT.h"
#define DHTPIN A0
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);
const int ledRojo = 13;
const int ledVerde = 11;
const int ledAzul = 9;

void setup() {
    Serial.begin(9600);
    Serial.println("Prueba de temperatura");
    dht.begin();
    pinMode(ledRojo, OUTPUT);
    pinMode(ledVerde, OUTPUT); 
    pinMode(ledAzul, OUTPUT);
}

void loop() {  
    delay(1000);
    
    float h = dht.readHumidity();
    float t = dht.readTemperature();
    float f = dht.readTemperature(true);
    if (t < 22.00){
      digitalWrite(ledRojo, LOW);
      digitalWrite(ledVerde, LOW);
      digitalWrite(ledAzul, HIGH);
      Serial.print("Hay frio = "); 
    }
    else if (t > 24.00){
      digitalWrite(ledRojo, HIGH);
      digitalWrite(ledVerde, LOW);
      digitalWrite(ledAzul, LOW);
      Serial.print("Hay calor = "); 
    }else {
      digitalWrite(ledRojo, LOW);
      digitalWrite(ledVerde, HIGH);
      digitalWrite(ledAzul, LOW);
      Serial.print("Esta fresco = "); 
    }
    
    if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
    }

    Serial.print("Humidity: ");
    Serial.print(h);
    Serial.print(" %\t");
    Serial.print("Temperature: ");
    Serial.println(t);
}
