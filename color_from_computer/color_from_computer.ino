#include <Adafruit_NeoPixel.h>

#define PIN            7
#define NUMPIXELS      21
#define NUM_LED_ON  9

typedef struct {
  byte r ;
  byte g ;
  byte b ;
} color ;

color led[NUMPIXELS];

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  Serial.begin(9600);
  pixels.begin();
  pixels.show(); // Initialize all pixels to 'off'
}

void loop() {
  if (Serial.available() >= (3*NUM_LED_ON)) {
    for (int i = 0 ; i < NUM_LED_ON  ; i++) {
    led[i].r = Serial.read();
    led[i].g = Serial.read();
    led[i].b = Serial.read();
    }
    for (int j = 0 ; j < NUM_LED_ON ; j++) {
    pixels.setPixelColor(j, pixels.Color(led[j].r , led[j].g, led[j].b));
    }
    pixels.show();
  }
}
