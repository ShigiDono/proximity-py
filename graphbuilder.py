import pyqtgraph as pg

class GraphBuilder(object):
	"""docstring for GraphBuilder"""
	def __init__(self, title, settings):
		self.win = pg.GraphicsWindow()
		self.win.setWindowTitle(title)
		self.data = []
		self.curves = []
		self.settings = settings
		for row in settings:
			row_data = []
			for cell in row:
				plot = self.win.addPlot()
				plot.setLabel("bottom", *(cell["bottom"] or ["",""]))
				plot.setLabel("left", *(cell["left"] or ["",""]))
				cell_data = []
				for curve_data in cell["curves"]:
					data = []
					curve = plot.plot(data, pen = pg.mkPen(color=curve_data["color"]))
					curve.data = data
					self.curves.append(curve)
					cell_data.append(data)
				row_data.append(cell_data)
			self.data.append(row_data)
			self.win.nextRow()
	def updateData(self, row, cell, data, curve=0):
		self.data[row][cell][curve].append(data)
		if len(self.data[row][cell][curve]) > self.settings[row][cell]["curves"][curve]["data_size"]:
			del self.data[row][cell][curve][0]
	def setData(self):
		for curve in self.curves:
			curve.setData(curve.data)