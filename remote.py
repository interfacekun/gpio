# -*- coding: utf-8 -*-    
import RPi.GPIO as GPIO    
import time
import os
# BOARD编号方式，基于插座引脚编号
GPIO.setwarnings(False)  
GPIO.setmode(GPIO.BOARD)    
# 输出模式    
GPIO.setup(33, GPIO.OUT)

GPIO.output(33, GPIO.LOW)

GPIO.output(33, GPIO.HIGH)
cm='/root/mypython/ra.py'
os.system(cm)
time.sleep(0.5)
GPIO.output(33, GPIO.LOW)

















		
