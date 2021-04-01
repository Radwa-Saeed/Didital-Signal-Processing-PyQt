
from newGui import Ui_MainWindow
import sys
from pyqtgraph import PlotWidget ,PlotItem
import os
import pathlib
import pyqtgraph as pg 
import pandas as pd
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets ,QtPrintSupport

#--------- to save as pdf ------------#
def print_widget(widget, filename):

    printer =QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
    printer.setOutputFormat(QtGui.QtPrintSupport.QPrinter.PdfFormat)
    printer.setOutputFileName(filename)
    painter = QtGui.QPainter(printer)

    # start scale
    xscale = printer.pageRect().width() * 1.0 / widget.width()
    yscale = printer.pageRect().height() * 1.0 / widget.height()
    scale = min(xscale, yscale)
    painter.translate(printer.paperRect().center())
    painter.scale(scale, scale)
    painter.translate(-widget.width() / 2, -widget.height() / 2)
    # end scale
    widget.render(painter)
    painter.end()

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionsiganl_1.triggered.connect(lambda:self.opensignal1())

    def readsignal1(self):
        self.fname1=QtGui.QFileDialog.getOpenFileName(self,'open only txt file',os.getenv('home'),"text(*.txt)")
        path=self.fname1[0]
        self.data1=np.genfromtxt(path)

    def opensignal1(self):
        self.readsignal1()
       
        self.data_line1 = self.ui.signal_1.plot(self.data1, name="mode2")
        self.ptr1 = 0
        self.n = 0

        # Set timer
        self.timer = pg.QtCore.QTimer()
        
        # Timer signal binding update_data function
        self.timer.timeout.connect(self.update_data)
        # The timer interval is 50ms, which can be understood as refreshing data once in 50ms
        self.timer.start(50)
        self.signal_1.show()
    #Data shift left
    def update_data(self):
        self.n += 10
        self.data_line1.setData(self.data1[0 : 100+self.n])
        self.data_line1.setPos(self.ptr1,0)
    
        #----- save as pdf ---#


    # def savepdf(self):
    #     fn, _ = QtWidgets.QFileDialog.getSaveFileName(
    #         self, "Export PDF", None, "PDF files (.pdf);;All Files()")
    #     if fn:
    #         if QtCore.QFileInfo(fn).suffix() == "": fn += ".pdf"
    #         print_widget(MainWindow , fn)



def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()