#!/usr/bin/env python
#-*- coding:utf-8 -*-
import time
import sys
import os 
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI
import Image
import ImageDraw
import ImageFont
import socket 
import struct 
import fcntl
import thread
import linecache

def getip(ethname): 
  
	s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
  
	return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0X8915, struct.pack('256s', ethname[:15]))[20:24])
#global ip
sayT=u'杰克码的树莓派'
ip='网络未连接'
ip=ip.decode('utf-8')
sleepTime=0.15
reset=-81
dec_x=11
stop_x=7
stop_time=0
judge1=1
temper=0
#global ip_x
ip_x=(LCD.LCDWIDTH-len(ip) * 10) / 2
lcdWidth=LCD.LCDWIDTH
def getIPThread():
	while True:
		try:
			global ip
			global ip_x
			ip=getip('wlan0')
			ip_x=(LCD.LCDWIDTH-len(ip) * 6) / 2
		except Exception,e:
			time.sleep(1)
			continue
		break
thread.start_new_thread(getIPThread,())
def readSayT():
	i=0
	global sayT
	global sleepTime
	global lcdWidth
	global reset
	global stop_x
	global dec_x
	global stop_time
	mstr='ddf'
	while True:
		txtTime=0.3
		try:
			f=open('/root/gpio/say.txt')
			fcntl.flock(f, fcntl.LOCK_EX)
			mstr1=f.readline().strip('\n').decode('utf-8')
			fcntl.flock(f,fcntl.LOCK_UN)
			if(mstr != mstr1):
				#print 'noequle'
				mstr=mstr1
				if( mstr.strip()):
					sayT=mstr
					sleepTime=0.5
					txtTime=((80+len(mstr)*10)/10 + 0.4)*0.5
					reset=85
					stop_x=85
					dec_x=10
					judge1=1
					stop_time=0
					lcdWidth=LCD.LCDWIDTH
					time.sleep(txtTime+1)
					lcdWidth=LCD.LCDWIDTH
					continue
				if(not mstr.strip()):
					print 'msg'
			sayT=u'杰克码的树莓派'
			reset=-81
			sleepTime=0.15
				#fcntl.flock(dec_x,fcntl.LOCK_EX)
			dec_x=11
				#fcntl.flock(dec_x,fcntl.LOCK_UN)
			if(judge1==0):
				#fcntl.flock(dec_x,fcntl.LOCK_EX)
				dec_x=0
				#fcntl.flock(dec_x,fcntl.LOCK_UN)
			stop_x=7
		except Exception,e:
			print e
			time.sleep(txtTime)
			continue
		time.sleep(txtTime)
thread.start_new_thread(readSayT,())
def getTemperature():
	global temper
	while True:
		tfile = open("/sys/bus/w1/devices/28-0415a14811ff/w1_slave")
		fcntl.flock(tfile, fcntl.LOCK_EX)
		text = tfile.read()
		fcntl.flock(tfile,fcntl.LOCK_UN)
		tfile.close()
		secondline = text.split("\n")[1]
		temperaturedata = secondline.split(" ")[9]
		temperature = float(temperaturedata[2:])
		temperature = temperature / 1000
		temper = int(temperature)
		time.sleep(60)
thread.start_new_thread(getTemperature,())
#time.sleep(20)
#bool_ip=True
#while bool_ip:
#	try:
#		ip=getip('wlan0')
#	except Exception,e:
#		continue
#	bool_ip=Flase
# Raspberry Pi hardware SPI config:
DC = 9
RST = 3
SPI_PORT = 0
SPI_DEVICE = 0

# Raspberry Pi software SPI config:
# SCLK = 4
# DIN = 17
# DC = 23
# RST = 24
# CS = 8

# Beaglebone Black hardware SPI config:
# DC = 'P9_15'
# RST = 'P9_12'
# SPI_PORT = 1
# SPI_DEVICE = 0

# Beaglebone Black software SPI config:
# DC = 'P9_15'
# RST = 'P9_12'
# SCLK = 'P8_7'
# DIN = 'P8_9'
# CS = 'P8_11'

# Hardware SPI usage:
disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Software SPI usage (defaults to bit-bang SPI interface):
#disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)

# Initialize library.
font = ImageFont.truetype('/root/gpio/yahei.ttf', 10)
disp.begin(contrast=60)
	# Clear display.
disp.clear()
disp.display()
while True:
	if(lcdWidth==reset):
		lcdWidth=LCD.LCDWIDTH
	if(lcdWidth==stop_x):
		judge1=0
		stop_time+=1
		dec_x=0
		if(stop_time==21):
			stop_time=0
			judge1=1
			#fcntl.flock(dec_x,fcntl.LOCK_EX)
			dec_x=11
			#fcntl.flock(dec_x,fcntl.LOCK_UN)
	# Create blank image for drawing.
	# Make sure to create image with mode '1' for 1-bit color.
	image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))

	# Get drawing object to draw on image.
	draw = ImageDraw.Draw(image)

	# Draw a white filled box to clear the image.
	draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
	#print LCD.LCDWIDTH 84
	#print LCD.LCDHEIGHT 48
	# Draw some shapes.
	#draw.ellipse((2,2,22,22), outline=0, fill=255)
	#draw.rectangle((24,2,44,22), outline=0, fill=255)
	#draw.polygon([(46,22), (56,2), (66,22)], outline=0, fill=255)
	#draw.line((68,22,81,2), fill=0)
	#draw.line((68,2,81,22), fill=0)
	

	# Load default font.
	#font = ImageFont.load_default()

	# Alternatively load a TTF font.
	# Some nice fonts to try: http://www.dafont.com/bitmap.php
	# font = ImageFont.truetype('Minecraftia.ttf', 8)
	# Write some text.
	ISOTIMEFORMAT='%Y-%m-%d'
	dateT=time.strftime(ISOTIMEFORMAT, time.localtime())
	dateT_x=(LCD.LCDWIDTH-len(dateT) * 6) / 2
	#print len(ip)
	#print len(dateT)
	draw.text((lcdWidth,3),sayT,font=font)
	draw.text((ip_x,16),ip,font=font)
	draw.text((dateT_x-12,26),dateT, font=font)
	draw.text((62,26),str(temper)+u'℃', font=font)
	
	ISOTIMEFORMAT='%H:%M:%S'
	timeT=time.strftime(ISOTIMEFORMAT, time.localtime())
	timeT_x=(LCD.LCDWIDTH-len(timeT) * 6) / 2
	draw.text((timeT_x,36),timeT, font=font)

	# Display image.
	disp.image(image)
	disp.display()
	lcdWidth-=dec_x
	time.sleep(sleepTime)
