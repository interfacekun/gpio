# -*- coding: utf-8 -*-    
import RPi.GPIO as GPIO    
import time    
# BOARD编号方式，基于插座引脚编号
GPIO.setwarnings(False)  
GPIO.setmode(GPIO.BOARD)    
# 输出模式    
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.output(31, GPIO.LOW)
GPIO.output(37, GPIO.LOW)
GPIO.output(35, GPIO.LOW)
i=0
while True:
	GPIO.output(35, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(35, GPIO.LOW)
	time.sleep(0.5)
	if i==20:
		i=0
	if (i>=0 and i<10):
		GPIO.output(31, GPIO.HIGH)
		GPIO.output(37, GPIO.LOW)
	elif (i>=10 and i<20):
		GPIO.output(31, GPIO.LOW)
                GPIO.output(37, GPIO.HIGH)
	i += 1
