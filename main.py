import serial
import numpy as np

import pyqtgraph as pg
import thread
from pyqtgraph.Qt import QtCore, QtGui



win = pg.GraphicsWindow()
win.setWindowTitle('pyqtgraph example: Scrolling Plots')

p1 = win.addPlot()
p2 = win.addPlot()
win.nextRow()
p3 = win.addPlot()
p4 = win.addPlot()
p1.setLabel('bottom', 'Time', 's')
p2.setLabel('bottom', 'Time', 's')
p3.setLabel('bottom', 'Time', 's')
p4.setLabel('bottom', 'Time', 's')
p1.setLabel('left', 'Proximity', '?')
p2.setLabel('left', 'IR Light', '?')
p3.setLabel('left', 'Visible light', '?')
p4.setLabel('left', 'UV Index', '?')

data11 = [0] * 1000
data12 = [0] * 1000
data13 = [0] * 1000
data2 = [0] * 1000
data3 = [0] * 1000
data4 = [0] * 1000

window_size, poly_order = 101, 3

curve11 = p1.plot(data11, pen = pg.mkPen(color=(255, 0, 0)))
curve12 = p1.plot(data12, pen = pg.mkPen(color=(0, 255, 0)))
curve13 = p1.plot(data13, pen = pg.mkPen(color=(0, 0, 255)))
curve2 = p2.plot(data2, pen = pg.mkPen(color=(200, 50, 50)))
curve3 = p3.plot(data3, pen = pg.mkPen(color=(100, 100, 255)))
curve4 = p4.plot(data4, pen = pg.mkPen(color=(200, 50, 255)))



ser = serial.Serial('/dev/ttyACM0', 230400, timeout=1)


 
# make plot

def update_data():
	global ser, data11, data12, data13, data2, data3, data4
	while ser.isOpen():
		l = ser.readline()
		numbers = [int(s) for s in l.split() if s.isdigit()]
		#print (numbers)
		if len(numbers) != 7:
			continue
		data11.append(numbers[4])
		del data11[0]
		data12.append(numbers[5])
		del data12[0]
		data13.append(numbers[6])
		del data13[0]

		data2.append(numbers[3])
		del data2[0]

		data3.append(numbers[2])
		del data3[0]

		data4.append(numbers[1])
		del data4[0]

thread.start_new_thread(update_data, ())


def update():
	global curve1, curve2, curve3, curve4
	curve11.setData(data11)
	curve12.setData(data12)
	curve13.setData(data13)
	curve2.setData(data2)
	curve3.setData(data3)
	curve4.setData(data4)

timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(1)



## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()