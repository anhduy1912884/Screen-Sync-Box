#include <Adafruit_NeoPixel.h>

#define PIN            7
#define NUMPIXELS      21
#define NUM_LED_ON  4
#define COLOR(x) pixels.Color(led[x].r , led[x].g, led[x].b)
int n ;
typedef struct {
  byte r ;
  byte g ;
  byte b ;
} color ;

color led[NUMPIXELS];

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  Serial.begin(57600);
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
    n = 0 ;
    for (int j = 0 ; j < NUM_LED_ON ; j++) {      
      pixels.setPixelColor(n, COLOR(j));
      n++ ;
      pixels.setPixelColor(n, COLOR(j));
      n++ ;
      pixels.setPixelColor(n, COLOR(j));
      n++ ;
      pixels.setPixelColor(n, COLOR(j));
      n++ ;
      pixels.setPixelColor(n, COLOR(j));
      n++ ;       
    }
    pixels.show();
  }
}

/*  
'''
x0 = 150
y0 = 900
x1 = 150
y1 = 530
x2 = 150
y2 = 150
x3 = 800
y3 = 200
x4 = 950
y4 = 200
x5 = 1500
y5 = 200
x6 = 1800
y6 = 150
x7 = 1800
y7 = 530
x8 = 1800
y8 = 900
'''

*/
