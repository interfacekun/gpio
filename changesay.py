import fcntl
import os
import sys
#i=0
#while True:
f=open('/root/gpio/say.txt','w')
fcntl.flock(f, fcntl.LOCK_EX)
f.write(sys.argv[1])
i=1
fcntl.flock(f, fcntl.LOCK_UN)
	#if(i==1):
	#	break
	#sleep(0.5)
	
