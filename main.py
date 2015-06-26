import serial

import thread
from pyqtgraph.Qt import QtCore, QtGui
from graphbuilder import GraphBuilder
import pyqtgraph as pg
from config import config, uart_device

ser = serial.Serial(uart_device, 230400, timeout=1)

graph = GraphBuilder('Proximity graph', config)
 
# make plot

def update_data():
	while ser.isOpen():
		l = ser.readline()
		numbers = [int(s) for s in l.split() if s.isdigit()]
		if len(numbers) != 7:
			continue
		graph.updateData(0, 0, 1.0/numbers[4])
		graph.updateData(0, 1, numbers[5])
		graph.updateData(0, 2, 1.0/numbers[6])
		graph.updateData(1, 0, numbers[3])
		graph.updateData(1, 1, numbers[2])
		graph.updateData(1, 2, numbers[1])

thread.start_new_thread(update_data, ())


def update():
	graph.setData()

timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(16)



## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()