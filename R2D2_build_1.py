import os
import sys
import time
import RPi.GPIO as GPIO
import PiFm
GPIO.setmode(GPIO.BCM)
import time

GPIO.setup(15, GPIO.IN, GPIO.PUD_DOWN) #checks for a change on pin 7

###Reset Motor
GPIO.setup(9, GPIO.OUT)
GPIO.output(9, GPIO.HIGH)

###Reset LED 
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, GPIO.LOW)

###Controls the LED eye
def LED_Eye():
    GPIO.output(21, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(21, GPIO.LOW)

print ("Welcome to R2D2")
motor_on = False    
       
while True:
    if GPIO.input(15) == 1:
        print ("You touched R2D2!")
        print ("Random STAR WARS FACT")
        motor_on = True

        '''Enable LED'''
        GPIO.output(9, GPIO.LOW)
        LED_Eye()

        '''Enable the Haptic Motor'''
        GPIO.output(9, GPIO.HIGH)

        '''start webcam'''
        os.system('service motion start')

        '''Play the Star Wars Theme'''      
        PiFm.play_sound("sound.wav")
            
        '''Stop the Webcam'''       
        os.system('service motion stop')
        
            
        


            
