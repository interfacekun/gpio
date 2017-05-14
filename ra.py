# -*- coding: utf-8 -*-    
import RPi.GPIO as GPIO    
import time
import os
# BOARD编号方式，基于插座引脚编号
GPIO.setwarnings(False)  
GPIO.setmode(GPIO.BOARD)    
# 输出模式    
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(36, GPIO.IN)
GPIO.output(33, GPIO.LOW)
GPIO.output(31, GPIO.LOW)
GPIO.output(37, GPIO.LOW)
GPIO.output(35, GPIO.LOW)

while True:
	in_key1=GPIO.input(36)
	if(in_key1==False):
		GPIO.output(33, GPIO.HIGH)
		cm='/root/mypython/ra.py'
		os.system(cm)
		time.sleep(0.5)
		GPIO.output(33, GPIO.LOW)
	time.sleep(0.2)

















		
