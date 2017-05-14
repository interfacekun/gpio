import RPi.GPIO as GPIO
import time

DS = 16

SHCP = 11

STCP = 26

GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)
GPIO.setup(DS, GPIO.OUT)
GPIO.setup(STCP, GPIO.OUT)
GPIO.setup(SHCP, GPIO.OUT)

GPIO.output(STCP, False)
GPIO.output(SHCP, False)

def setBitData(data):
	GPIO.output(DS, data)
	GPIO.output(SHCP, False)
	GPIO.output(SHCP, True)
	#time.sleep(0.5)
def showDigit(num, showDotPoint):
	
	if (num == 0) :
		setBitData(True) #A
		setBitData(True)# B
		setBitData(True) # C
		setBitData(True) # D
		setBitData(True) # E
		setBitData(True) # F
		setBitData(False) # G
		setBitData(showDotPoint) # DP
	elif (num == 1) :
		setBitData(False)
		setBitData(True)
		setBitData(True)
		setBitData(False)
		setBitData(False)
		setBitData(False)
		setBitData(False)
		setBitData(showDotPoint)
	elif (num == 2) :
		setBitData(True)
		setBitData(True)
		setBitData(False)
		setBitData(True)
		setBitData(True)
		setBitData(False)
		setBitData(True)
		setBitData(showDotPoint)
	elif (num == 3) :
		setBitData(True)
		setBitData(True)
		setBitData(True)
		setBitData(True)
		setBitData(False)
		setBitData(False)
		setBitData(True)
		setBitData(showDotPoint)
	elif (num == 9) :
		setBitData(True)
		setBitData(True)
		setBitData(True)
		setBitData(True)
		setBitData(False)
		setBitData(True)
		setBitData(True)
		setBitData(showDotPoint)
	elif (num == 5) :
		setBitData(True)
		setBitData(False)
		setBitData(True)
		setBitData(True)
		setBitData(False)
		setBitData(True)
		setBitData(True)
		setBitData(showDotPoint)
	elif (num == 6) :
		setBitData(True)
		setBitData(False)
		setBitData(True)
		setBitData(True)
		setBitData(True)
		setBitData(True)
		setBitData(True)
		setBitData(showDotPoint)
	elif (num == 7) :
		setBitData(True)
		setBitData(True)
		setBitData(True)
		setBitData(False)
		setBitData(False)
		setBitData(False)
		setBitData(False)
		setBitData(showDotPoint)
	elif (num == 8) :
		setBitData(True)
		setBitData(True)
		setBitData(True)
		setBitData(True)
		setBitData(True)
		setBitData(True)
		setBitData(True)
		setBitData(False)
	elif (num == 4) :
		setBitData(False)
		setBitData(True)
		setBitData(True)
		setBitData(False)
		setBitData(False)
		setBitData(True)
		setBitData(True)
		setBitData(showDotPoint)

	GPIO.output(STCP, False)
	GPIO.output(STCP, True)

try:
	i=0
	while True:
		if i==10:
			i=0
		showDigit(i, False)
		time.sleep(1)
		i+=1
except KeyboardInterrupt:
	pass
GPIO.cleanup()
