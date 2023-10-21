#include <Adafruit_NeoPixel.h>

#define PIN            7
#define NUMPIXELS      21

typedef struct {
  byte r ;
  byte g ;
  byte b ;
} color ;

color led[21];

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  Serial.begin(9600);
  pixels.begin();
  pixels.show(); // Initialize all pixels to 'off'
}

void loop() {
  int n = 3 ;
  if (Serial.available() >= 6) {
    for (int i = 0 ; i < 6 ; i+= n) {
    led[i].r = Serial.read();
    led[i].g = Serial.read();
    led[i].b = Serial.read();
    }
   // int n = 3 ;
    for (int j = 0 ; j <6 ; j+= 3) {
    pixels.setPixelColor(j, pixels.Color(led[j].r , led[j].g, led[j].b));
    pixels.setPixelColor(j+1, pixels.Color(led[j].r , led[j].g, led[j].b));
    pixels.setPixelColor(j+2, pixels.Color(led[j].r , led[j].g, led[j].b));
    }
    pixels.show();
  }
}
