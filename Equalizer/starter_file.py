
from SignalViewer import Ui_MainWindow
from another import Ui_MainWindow2
import sys
from pyqtgraph import PlotWidget ,PlotItem
import os
import pathlib
import pyqtgraph as pg 
import pandas as pd
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets ,QtPrintSupport

class Anotherwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui2 = Ui_MainWindow2()
        self.ui2.setupUi(self)


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.new.clicked.connect(lambda:self.newwindow())

    def newwindow (self):
            self.window=Ui_MainWindow2()
            self.window.show()   

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()