#include <Adafruit_NeoPixel.h>

#define PIN            7
#define NUMPIXELS      21

typedef struct {
  byte r ;
  byte g ;
  byte b ;
} color ;

color led[NUMPIXELS];

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  Serial.begin(115200);
  pixels.begin();
  pixels.show(); // Initialize all pixels to 'off'
}

void loop() {
  if (Serial.available() >= (63)) {
    for (int i = 0 ; i < NUMPIXELS  ; i++) {
    led[i].r = Serial.read();
    led[i].g = Serial.read();
    led[i].b = Serial.read();
    }
   // int n = 3 ;
    for (int j = 0 ; j < NUMPIXELS ; j++) {
    pixels.setPixelColor(j, pixels.Color(led[j].r , led[j].g, led[j].b));
    pixels.setPixelColor(j+1, pixels.Color(led[j].r , led[j].g, led[j].b));
    pixels.setPixelColor(j+2, pixels.Color(led[j].r , led[j].g, led[j].b));
    }
    pixels.show();
  }
}
