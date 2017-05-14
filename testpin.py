# -*- coding: utf-8 -*-    
import RPi.GPIO as GPIO    
import time    
# BOARD编号方式，基于插座引脚编号
GPIO.setwarnings(False)  
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.LOW)
while True:
	GPIO.output(22, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(22, GPIO.LOW)
	time.sleep(1)
