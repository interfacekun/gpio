
tfile = open("/sys/bus/w1/devices/28-0415a14811ff/w1_slave")
text = tfile.read()
tfile.close()
secondline = text.split("\n")[1]
temperaturedata = secondline.split(" ")[9]
temperature = float(temperaturedata[2:])
temperature = temperature / 1000
print int(temperature)
