# -*- coding: utf-8 -*-    
import RPi.GPIO as GPIO    
import time
GPIO.setwarnings(False)  
GPIO.setmode(GPIO.BOARD)    
GPIO.setup(33,GPIO.OUT)

for i in range(1,4): 
	GPIO.output(33, GPIO.HIGH)
	time.sleep(0.2)
	GPIO.output(33,GPIO.LOW)
	time.sleep(0.2)
