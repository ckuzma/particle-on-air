// This #include statement was automatically added by the Particle IDE.
#include <HC-SR04.h>

// Pins
const int TRIGGERPIN = A0;
const int ECHOPIN = D0;
const int LED_PIN = D1;

// Labels for our data
char distLabel[] = "distance-inch";

// Set sampling rates
int distSampleTime = 10; // Sampling rate
int sampleDelay = 2000; // How often we take a sample and report it
float distanceThresh = 1.5;
int loopsRequired = 10;
bool doorOpen = false;

// Instantiate the library
HC_SR04 rangefinder = HC_SR04(TRIGGERPIN, ECHOPIN);

void setup() {
    pinMode(LED_PIN, OUTPUT);
    rangefinder.init();
}

void loop() {
    // Get distance measurement
    float inch = getDistance();
    
    // Get door open/closed
    bool newDoor = doorChange(inch);
    
    // Flash the sign if closed
    doorFlash(newDoor);
    
    // Change publish
    if (newDoor != doorOpen) {
        Particle.publish(distLabel, String(inch));
        doorOpen = newDoor;
    }
    
    // Heartbeat publish + iterate
    if (loopsRequired == 0) {
        Particle.publish(distLabel, String(inch));
        loopsRequired = 60;
    }
    loopsRequired--;
}

float getDistance() {
    // Get distance measurement in inches
    float inch = rangefinder.distInch();
    return inch;
}

bool doorChange(float inch) {
    if (inch < distanceThresh) {
        return false;
    }
    else {
        return true;
    }
}

void doorFlash(bool newDoor) {
    if (newDoor == false) {
        digitalWrite(LED_PIN, LOW);
        delay(400);
        digitalWrite(LED_PIN, HIGH);
        delay(800);
        digitalWrite(LED_PIN, LOW);
        delay(400);
    }
    else {
        delay(1600);
    }
}