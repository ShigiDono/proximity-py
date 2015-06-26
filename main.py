import serial
import numpy as np
from matplotlib import pyplot as plt


ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

plt.ion()

ydata = [0] * 50

ax1=plt.axes()  
 
# make plot
line, = plt.plot(ydata)
plt.ylim([200,1000]) # set the y-range to 10 to 40

while (ser.isOpen()):
	l = ser.readline()
	numbers = [int(s) for s in l.split() if s.isdigit()]
	print (numbers)
	if len(numbers) != 5:
		continue
	ydata.append(numbers[4])
	del ydata[0]
	#ymin = float(min(ydata))-10
	#ymax = float(max(ydata))+10
	#plt.ylim([ymin,ymax])
	line.set_xdata(np.arange(len(ydata)))
	line.set_ydata(ydata)  # update the data
	plt.draw() # update the plot