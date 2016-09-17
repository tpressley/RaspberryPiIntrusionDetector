import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.OUT)
GPIO.output(19,GPIO.LOW)

def checkForFailedPasswordLogin():
        i = 0
        last = ""
        prev = last
        found = 0
        while(i < 10):
                f = open("/var/log/auth.log")
                for line in f:
                        last = line
                if "Failed password" in last and found == 0:
                        print last
                        found = 1
                        GPIO.output(19,GPIO.HIGH)
                        time.sleep(3)
                        GPIO.output(19,GPIO.LOW)
                if last != prev:
                        prev = last
                        found = 0


checkForFailedPasswordLogin()
GPIO.cleanup()
