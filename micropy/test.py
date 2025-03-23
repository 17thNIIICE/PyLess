from machine import Pin
import time 

_init() 

LedPin = 16 

led = Pin(LedPin, Pin.OUT)

while True:
    led.off()
    time.sleep(5)
    led.on()
    time.sleep(0.1)

