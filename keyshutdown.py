# -*- coding: utf-8 -*-    
import RPi.GPIO as GPIO    
import time
import os
# BOARD编号方式，基于插座引脚编号
GPIO.setwarnings(False)  
GPIO.setmode(GPIO.BOARD)    
# 输出模式
GPIO.setup(33,GPIO.OUT)    
GPIO.setup(40, GPIO.IN)
GPIO.setup(38,GPIO.IN)

while True:
	in_key3=GPIO.input(40)
	in_key2=GPIO.input(38)
	if(in_key3==False):
		GPIO.output(33, GPIO.HIGH)
		cm='shutdown -h now'
		os.system(cm)
		time.sleep(0.5)
		GPIO.output(33, GPIO.LOW)
	if(in_key2==False):
		GPIO.output(33,GPIO.HIGH)
		cm='sudo -u root irexec -d'
		os.system(cm)
		time.sleep(0.5)
		GPIO.output(33,GPIO.LOW)
	time.sleep(0.2)


















		
