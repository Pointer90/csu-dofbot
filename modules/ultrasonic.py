import RPi.GPIO as GPIO
import time

class Ultrasonic:
    EchoPin = 0
    TrigPin = 1

    def __init__(self):
        GPIO.setup(self.EchoPin,GPIO.IN)
        GPIO.setup(self.TrigPin,GPIO.OUT)