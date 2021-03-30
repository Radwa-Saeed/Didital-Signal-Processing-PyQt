# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtGui, QtWidgets ,QtPrintSupport
from pyqtgraph import PlotWidget ,PlotItem
import os
import pathlib
import pyqtgraph as pg 
import pandas as pd
import numpy as np

import sys
import random
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


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

class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class Ui_MainWindow(QtGui.QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1010, 878)
        mW = QtGui.QIcon("Mw.png")
        MainWindow.setWindowIcon(mW)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.signal_1 = PlotWidget(self.centralwidget)
        self.signal_1.setGeometry(QtCore.QRect(20, 90, 461, 192))
        self.signal_1.setStyleSheet("background-color:rgb(0, 0, 0);")
        self.signal_1.setRubberBandSelectionMode(QtCore.Qt.IntersectsItemBoundingRect)
        self.signal_1.setObjectName("signal_1")
        self.signal_1.plotItem.showGrid(x=True, y=True )
        self.signal_1.plotItem.setMenuEnabled(False)

        self.signal_2 = PlotWidget(self.centralwidget)
        self.signal_2.setGeometry(QtCore.QRect(20, 340, 461, 192))
        self.signal_2.setStyleSheet("background-color:rgb(0, 0, 0);")
        self.signal_2.setRubberBandSelectionMode(QtCore.Qt.IntersectsItemBoundingRect)
        self.signal_2.setObjectName("signal_2")
        self.signal_2.plotItem.showGrid(x=True, y=True )
        self.signal_2.plotItem.setMenuEnabled(False)

        self.signal_3 = PlotWidget(self.centralwidget)
        self.signal_3.setGeometry(QtCore.QRect(20, 600, 461, 192))
        self.signal_3.setStyleSheet("background-color:rgb(0, 0, 0);")
        self.signal_3.setRubberBandSelectionMode(QtCore.Qt.IntersectsItemBoundingRect)
        self.signal_3.setObjectName("signal_3")
        self.signal_3.plotItem.showGrid(x=True, y=True )
        self.signal_3.plotItem.setMenuEnabled(False)

        self.spectro_1 = QtWidgets.QLabel(self.centralwidget)
        self.spectro_1.setScaledContents(True)
        self.spectro_1.setGeometry(QtCore.QRect(490, 90, 471, 192))
        self.spectro_1.setObjectName("spectro_1")
        
        self.spectro_2 = QtWidgets.QLabel(self.centralwidget)
        self.spectro_2.setScaledContents(True)
        self.spectro_2.setGeometry(QtCore.QRect(490, 340, 471, 192))
        self.spectro_2.setObjectName("spectro_2")

        self.spectro_3 = QtWidgets.QLabel(self.centralwidget)
        self.spectro_3.setScaledContents(True)
        self.spectro_3.setGeometry(QtCore.QRect(490, 600, 471, 192))
        self.spectro_3.setObjectName("spectro_3")
    
        self.check_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_1.setGeometry(QtCore.QRect(20, 50, 68, 20))
        self.check_1.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.check_1.setObjectName("check_1")

        self.check_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_2.setGeometry(QtCore.QRect(20, 300, 68, 20))
        self.check_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.check_2.setObjectName("check_2")

        self.check_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_3.setGeometry(QtCore.QRect(20, 560, 68, 20))
        self.check_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.check_3.setObjectName("check_3")


        self.check_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_4.setGeometry(QtCore.QRect(20, 780, 68, 20))
        self.check_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.check_4.setObjectName("check_4")



    
     
       
        self.Zoom_in = QtWidgets.QPushButton(self.centralwidget)
        self.Zoom_in.setGeometry(QtCore.QRect(10, 1, 35, 35))
        self.Zoom_in.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Zoom_in.setIcon(icon)
        self.Zoom_in.setObjectName("Zoom_in")

        self.zoom_out = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_out.setGeometry(QtCore.QRect(50, 1, 35, 35))
        self.zoom_out.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("zoom-ou.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_out.setIcon(icon1)
        self.zoom_out.setObjectName("zoom_out")

        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(370, 1, 35, 35))
        self.save.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save.setIcon(icon2)
        self.save.setObjectName("save")

        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(250, 1, 35, 35))
        self.clear.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("eraser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear.setIcon(icon3)
        self.clear.setObjectName("clear")

        self.pause = QtWidgets.QPushButton(self.centralwidget)
        self.pause.setGeometry(QtCore.QRect(210, 1, 35, 35))
        self.pause.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause.setIcon(icon4)
        self.pause.setObjectName("pause")

        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setGeometry(QtCore.QRect(170, 1, 35, 35))
        self.play.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon5)
        self.play.setObjectName("play")

        self.delete = QtWidgets.QPushButton(self.centralwidget)
        self.delete.setGeometry(QtCore.QRect(290, 1, 35, 35))
        self.delete.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete.setIcon(icon10)
        self.delete.setObjectName("delete")


        self.right = QtWidgets.QPushButton(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(130, 1, 35, 35))
        self.right.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.right.setIcon(icon6)
        self.right.setObjectName("right")

        self.left = QtWidgets.QPushButton(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(90, 1, 35, 35))
        self.left.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.left.setIcon(icon7)
        self.left.setObjectName("left")

        self.spec = QtWidgets.QPushButton(self.centralwidget)
        self.spec.setGeometry(QtCore.QRect(330, 1, 35, 35))
        self.spec.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("spec3.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.spec.setIcon(icon20)
        self.spec.setObjectName("spec")

        self.Zoom_in.raise_()
        self.signal_1.raise_()
        self.check_2.raise_()
        self.spectro_2.raise_()
        self.spectro_3.raise_()
        self.check_3.raise_()
        self.spectro_1.raise_()
        self.signal_2.raise_()
        self.signal_3.raise_()
        self.check_1.raise_()
        self.zoom_out.raise_()
        self.save.raise_()
        self.clear.raise_()
        self.pause.raise_()
        self.play.raise_()
        self.right.raise_()
        self.left.raise_()
       
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1010, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuopen = QtWidgets.QMenu(self.menuFile)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuopen.setIcon(icon9)
        self.menuopen.setObjectName("menuopen")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSignal_tools = QtWidgets.QMenu(self.menubar)
        self.menuSignal_tools.setObjectName("menuSignal_tools")
        self.menuPlay_navigate = QtWidgets.QMenu(self.menubar)
        self.menuPlay_navigate.setObjectName("menuPlay_navigate")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsiganl_1 = QtWidgets.QAction(MainWindow)
        self.actionsiganl_1.setObjectName("actionsiganl_1")
        self.actionsignal_2 = QtWidgets.QAction(MainWindow)
        self.actionsignal_2.setObjectName("actionsignal_2")
        self.actionsignal_3 = QtWidgets.QAction(MainWindow)
        self.actionsignal_3.setObjectName("actionsignal_3")
        self.actionzoom_in = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("zoom-in_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionzoom_in.setIcon(icon10)
        self.actionzoom_in.setObjectName("actionzoom_in")
        self.actionzoom_out = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("zoom-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionzoom_out.setIcon(icon11)
        self.actionzoom_out.setObjectName("actionzoom_out")
        # self.actionscroll_left = QtWidgets.QAction(MainWindow)
        # self.actionscroll_left.setObjectName("actionscroll_left")
        # self.actionscroll_right = QtWidgets.QAction(MainWindow)
        # self.actionscroll_right.setObjectName("actionscroll_right")
        # self.actionsavs_as_pdf = QtWidgets.QAction(MainWindow)
        # self.actionsavs_as_pdf.setObjectName("actionsavs_as_pdf")
        self.actionSpectrogram = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("sound.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSpectrogram.setIcon(icon12)
        self.actionSpectrogram.setObjectName("actionSpectrogram")
        self.actionPlay = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("play-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlay.setIcon(icon13)
        self.actionPlay.setObjectName("actionPlay")
        self.actionPause = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("pause-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPause.setIcon(icon14)
        self.actionPause.setObjectName("actionPause")
        self.actionStop = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("rubber.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop.setIcon(icon15)
        self.actionStop.setObjectName("actionStop")
        self.actionBackward = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("backward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBackward.setIcon(icon16)
        self.actionBackward.setObjectName("actionBackward")
        self.actionForward = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionForward.setIcon(icon17)
        self.actionForward.setObjectName("actionForward")
        self.actionSave_as_pdf = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("pdf-file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as_pdf.setIcon(icon18)
        self.actionSave_as_pdf.setObjectName("actionSave_as_pdf")
        self.menuopen.addAction(self.actionsiganl_1)
        self.menuopen.addAction(self.actionsignal_2)
        self.menuopen.addAction(self.actionsignal_3)
        self.menuFile.addAction(self.menuopen.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_as_pdf)
        self.menuEdit.addAction(self.actionzoom_in)
        self.menuEdit.addAction(self.actionzoom_out)
        self.menuSignal_tools.addAction(self.actionSpectrogram)
        self.menuPlay_navigate.addAction(self.actionPlay)
        self.menuPlay_navigate.addAction(self.actionPause)
        self.menuPlay_navigate.addAction(self.actionStop)
        self.menuPlay_navigate.addSeparator()
        self.menuPlay_navigate.addAction(self.actionBackward)
        self.menuPlay_navigate.addAction(self.actionForward)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuPlay_navigate.menuAction())
        self.menubar.addAction(self.menuSignal_tools.menuAction())
        self.signal_1.hide()
        self.check_1.hide()
        self.spectro_1.hide()
        self.signal_2.hide()
        self.check_2.hide()
        self.spectro_2.hide() 
        self.signal_3.hide()
        self.check_3.hide()
        self.spectro_3.hide()
       
    
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.r1=300
        self.r2=300
        self.r3=300
        self.actionsiganl_1.triggered.connect(lambda:self.opensignal1())
        self.actionsignal_2.triggered.connect(lambda:self.opensignal2())
        self.actionsignal_3.triggered.connect(lambda:self.opensignal3())
        self.actionzoom_in.triggered.connect(lambda:self.zoomin())
        self.actionzoom_out.triggered.connect(lambda:self.zoomout())
        self.actionSave_as_pdf.triggered.connect(lambda:self.savepdf())
        self.actionBackward.triggered.connect(lambda:self.scrlleft())
        self.actionForward.triggered.connect(lambda:self.scrlright())
        self.actionPlay.triggered.connect(lambda:self.playy())
        self.actionPause.triggered.connect(lambda:self.pausee())
        self.actionStop.triggered.connect(lambda:self.clearr())

        self.Zoom_in.clicked.connect(lambda:self.zoomin())
        self.zoom_out.clicked.connect(lambda:self.zoomout())
        self.left.clicked.connect(lambda:self.scrlleft())
        self.right.clicked.connect(lambda:self.scrlright())
        self.pause.clicked.connect(lambda:self.pausee())
        self.play.clicked.connect(lambda:self.playy())
        self.clear.clicked.connect(lambda:self.clearr())
        self.delete.clicked.connect(lambda:self.deletee())
        self.save.clicked.connect(lambda:self.savepdf())
        self.spec.clicked.connect(lambda:self.spectro())

    # def opensignal1(self):
    #     self.readsignal1()   
    #     self.data_line1 = self.signal_1.plot(self.data1, name="mode2")
    #     self.ptr1 = 0
    #     self.n1 = 0
    #     # Set timer
    #     self.timer1 = pg.QtCore.QTimer()
    #     # Timer signal binding update_data function
    #     self.timer1.timeout.connect(self.update_data1)
    #     # The timer interval is 50ms, which can be understood as refreshing data once in 50ms
    #     self.timer1.start(50)
    #     self.signal_1.show()
    #     self.check_1.show()
    #     self.spectro_1.show()
    #     self.check_1.setChecked(True)
           
    # #Data shift left
    # def update_data1(self):
    #     self.n1 += 10
    #     self.data_line1.setData(self.data1[0 : 100+self.n1])
    #     self.data_line1.setPos(self.ptr1,0)
        

    def readsignal1(self):
        self.fname1=QtGui.QFileDialog.getOpenFileName(self,'open only txt or CSV or xls',os.getenv('home'),"text(*.txt) ;; csv(*.csv) ;; xls(*.xls)")
        path=self.fname1[0]
        self.data1=np.genfromtxt(path)
        

    def readsignal2(self):
        self.fname2=QtGui.QFileDialog.getOpenFileName(self,'open only txt or CSV or xls',os.getenv('home'),"text(*.txt) ;; csv(*.csv) ;; xls(*.xls)")
        path=self.fname2[0]
        self.data2=np.genfromtxt(path)

    def readsignal3(self):
        self.fname3=QtGui.QFileDialog.getOpenFileName(self,'open only txt or CSV or xls',os.getenv('home'),"text(*.txt) ;; csv(*.csv) ;; xls(*.xls)")
        path=self.fname3[0]
        self.data3=np.genfromtxt(path)


    def opensignal1(self):
        self.readsignal1()
        self.h1 =len(self.data1)
        self.n1 = 0
        self.data_line1 = self.signal_1.plot(self.data1, name="mode2")
        self.pen = pg.mkPen(color=(255, 0, 0))
        # Set timer
        self.timer1 = pg.QtCore.QTimer()
        # Timer signal binding update_data function
        self.timer1.timeout.connect(self.update_data)
        # The timer interval is 50ms, which can be understood as refreshing data once in 50ms
        self.timer1.start(50)
       # self.timer1.start(50)
        self.signal_1.show()
        self.check_1.show()
        self.spectro_1.show()
        self.check_1.setChecked(True)
        # self.Viewsig_1.plotItem.setXRange(min(self.timer, default=0)+self.x)
    def opensignal2(self):
        self.readsignal2()   
        self.h2 =len(self.data2)
        self.n2 = 0
        self.data_line2 = self.signal_2.plot(self.data2, name="mode2")
        self.pen = pg.mkPen(color=(0, 255, 0))
        # Set timer
        self.timer2 = pg.QtCore.QTimer()
        # Timer signal binding update_data function
        self.timer2.timeout.connect(self.update_data2)
        # The timer interval is 50ms, which can be understood as refreshing data once in 50ms
        self.timer2.start(50)
        self.signal_2.show()
        self.check_2.show()
        self.spectro_2.show()
        self.check_2.setChecked(True)

    
    def opensignal3(self):
        self.readsignal3()   
        self.h3 =len(self.data3)
        self.n3 = 0
        self.data_line3 = self.signal_3.plot(self.data3, name="mode2")
        self.pen = pg.mkPen(color=(0, 0, 255))
        # Set timer
        self.timer3 = pg.QtCore.QTimer()
        # Timer signal binding update_data function
        self.timer3.timeout.connect(self.update_data3)
        # The timer interval is 50ms, which can be understood as refreshing data once in 50ms
        self.timer3.start(50)
        self.signal_3.show()
        self.check_3.show()
        self.spectro_3.show()
        self.check_3.setChecked(True)
      
    # Data shift left
    def update_data(self):
        if self.n1 < self.h1 :
            self.n1 += 10  
            self.data_line1.setData(self.data1[0 : 100+self.n1])
            self.signal_1.plotItem.setXRange(0+self.n1,self.r1+self.n1 , padding=0)
        else :
            self.data_line1.setData(self.data1[0 : 100+self.n1])
            self.signal_1.plotItem.setXRange(self.h1-1000 , self.h1 , padding=0)

    #Data shift left
    def update_data2(self):
        if self.n2< self.h2 :
            self.n2 += 10  
            self.data_line2.setData(self.data2[0 : 100+self.n2])
            self.signal_2.plotItem.setXRange(0+self.n2,self.r2+self.n2, padding=0)
        else :
            self.data_line2.setData(self.data1[0 : 100+self.n2])
            self.signal_2.plotItem.setXRange(self.h2-1000 , self.h2 , padding=0)
        # self.n2 += 10
        # self.data_line2.setData(self.data2[0 : 100+self.n2])
        # self.data_line2.setPos(self.ptr2,0)   
    #Data shift left
    def update_data3(self):
        if self.n3< self.h3 :
            self.n3 += 10  
            self.data_line3.setData(self.data3[0 : 100+self.n3])
            self.signal_3.plotItem.setXRange(0+self.n3,self.r3+self.n3, padding=0)
        else :
            self.data_line3.setData(self.data3[0 : 100+self.n3])
            self.signal_3.plotItem.setXRange(self.h3-1000 , self.h3 , padding=0)
        # self.n3 += 10
        # self.data_line3.setData(self.data3[0 : 100+self.n3])
        # self.data_line3.setPos(self.ptr3,0)


########################

    def spec1(self):
        self.x1data = self.data1
        self.ydata = list (range(11, 1+self.h1))
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        plt.specgram(self.x1data, Fs= 250)
        plt.savefig('spectro1.png', dpi=300, bbox_inches='tight')
        self.spectro_1.setPixmap(QtGui.QPixmap('spectro1.png'))

    def spec2(self):
        self.x2data = self.data2
        self.ydata = list (range(11, 1+self.h2))
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        plt.specgram(self.x2data, Fs= 250)
        plt.savefig('spectro2.png', dpi=300, bbox_inches='tight')
        self.spectro_2.setPixmap(QtGui.QPixmap('spectro2.png'))


    def spec3(self):
        self.x3data = self.data3
        self.ydata = list (range(11, 1+self.h3))
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        plt.specgram(self.x3data, Fs= 250)
        plt.savefig('spectro3.png', dpi=300, bbox_inches='tight')
        self.spectro_3.setPixmap(QtGui.QPixmap('spectro3.png'))


    def spectro(self):
        if (self.check_1.isChecked()==True):
            self.spec1()
            
        if (self.check_2.isChecked()==True):
            self.spec2()

        if (self.check_3.isChecked()==True):
            self.spec3()


########################

    def pausee(self):
        if (self.check_1.isChecked()==True):
            if self.timer1.isActive():
                self.timer1.stop()
        if (self.check_2.isChecked()==True):
            if self.timer2.isActive():
                self.timer2.stop()
        if (self.check_3.isChecked()==True):
            if self.timer3.isActive():
                self.timer3.stop()
    
    def playy(self):
        if (self.check_1.isChecked()==True):
            if self.timer1.isActive()==False:
                self.timer1.start()
        if (self.check_2.isChecked()==True):
            if self.timer2.isActive()==False:
                self.timer2.start()
        if (self.check_3.isChecked()==True):
            if self.timer3.isActive()==False:
                self.timer3.start()
     
        
        
    def zoomin(self):
        if (self.check_1.isChecked()==True):
            self.signal_1.plotItem.getViewBox().scaleBy(x=0.5,y=1)
            self.r1=self.r1*0.5
        if (self.check_2.isChecked()==True):
            self.signal_2.plotItem.getViewBox().scaleBy(x=0.5,y=1)  
            self.r2=self.r2*0.5
        if (self.check_3.isChecked()==True):
            self.signal_3.plotItem.getViewBox().scaleBy(x=0.5,y=1)
            self.r3=self.r3*0.5
        # else:
        #     pass
        
    def zoomout(self):
        if (self.check_1.isChecked()==True):
            self.signal_1.plotItem.getViewBox().scaleBy(x=2,y=1)
            self.r1=self.r1*2
        if (self.check_2.isChecked()==True):
            self.signal_2.plotItem.getViewBox().scaleBy(x=2,y=1)
            self.r2=self.r2*2  
        if (self.check_3.isChecked()==True):
            self.signal_3.plotItem.getViewBox().scaleBy(x=2,y=1)
            self.r3=self.r3*2

    def scrlleft(self):
        if (self.check_1.isChecked()==True):
            self.signal_1.plotItem.getViewBox().translateBy(x=-100,y=0)
        if (self.check_2.isChecked()==True):
            self.signal_2.plotItem.getViewBox().translateBy(x=-100,y=0)  
        if (self.check_3.isChecked()==True):
            self.signal_3.plotItem.getViewBox().translateBy(x=-100,y=0)

    def scrlright(self):
        if (self.check_1.isChecked()==True):
            self.signal_1.plotItem.getViewBox().translateBy(x=100,y=0)
        if (self.check_2.isChecked()==True):
            self.signal_2.plotItem.getViewBox().translateBy(x=100,y=0)  
        if (self.check_3.isChecked()==True):
            self.signal_3.plotItem.getViewBox().translateBy(x=100,y=0)
    # else:
    def clearr(self):
        if (self.check_1.isChecked()==True):
            if self.signal_1.clear()==False:
                self.signal_1.clear()
        #    self.spectro_1.clear()
                self.timer1= None
                self.data_line1.setData(self.data1[0 : 100])
        if (self.check_2.isChecked()==True):
            if self.signal_2.clear()==False:
                self.signal_2.clear()
        #    self.spectro_2.clear()
                self.timer2= None
                self.data_line2.setData(self.data1[0 : 100])
        if (self.check_3.isChecked()==True):
            if self.signal_3.clear()==False:
                self.signal_3.clear()
        #   self.spectro_3.clear()
                self.timer3= None
                self.data_line3.setData(self.data1[0 : 100])

    def deletee(self):
            if (self.check_1.isChecked()==True):
                self.signal_1.hide()
                self.spectro_1.hide()
                self.check_1.hide()
            if (self.check_2.isChecked()==True):
                self.signal_2.hide()
                self.spectro_2.hide()
                self.check_2.hide()
            if (self.check_3.isChecked()==True):
                self.signal_3.hide()
                self.spectro_3.hide()
                self.check_3.hide()
            
   
    #----- save as pdf ---#
    #----- save as pdf ---#


    def savepdf(self):
        fn, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Export PDF", None, "PDF files (.pdf);;All Files()")
        if fn:
            if QtCore.QFileInfo(fn).suffix() == "": fn += ".pdf"
            print_widget(MainWindow , fn)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.check_2.setText(_translate("MainWindow", "signal-2"))
        self.check_2.setShortcut(_translate("MainWindow", "2"))
        self.check_3.setText(_translate("MainWindow", "signal-3"))
        self.check_3.setShortcut(_translate("MainWindow", "3"))
        self.check_1.setText(_translate("MainWindow", "signal-1"))
        self.check_1.setShortcut(_translate("MainWindow", "1"))
        # self.clear.setShortcut(_translate("MainWindow", "Esc"))
        # self.pause.setShortcut(_translate("MainWindow", "Shift+Space"))
        # self.play.setShortcut(_translate("MainWindow", "Space"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuopen.setTitle(_translate("MainWindow", "Open"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuSignal_tools.setTitle(_translate("MainWindow", "Signal tools"))
        self.menuPlay_navigate.setTitle(_translate("MainWindow", "Play and navigate "))
        self.actionsiganl_1.setText(_translate("MainWindow", "siganl-1"))
        self.actionsiganl_1.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.actionsignal_2.setText(_translate("MainWindow", "signal-2"))
        self.actionsignal_2.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.actionsignal_3.setText(_translate("MainWindow", "signal-3"))
        self.actionsignal_3.setShortcut(_translate("MainWindow", "Ctrl+3"))
        self.actionzoom_in.setText(_translate("MainWindow", "Zoom-in"))
        self.actionzoom_in.setShortcut(_translate("MainWindow", "Up"))
        self.actionzoom_out.setText(_translate("MainWindow", "Zoom-out"))
        self.actionzoom_out.setShortcut(_translate("MainWindow", "Down"))
        self.actionSpectrogram.setText(_translate("MainWindow", "Spectrogram"))
        self.actionSpectrogram.setShortcut(_translate("MainWindow", "S"))
        self.actionPlay.setText(_translate("MainWindow", "Play"))
        self.actionPlay.setShortcut(_translate("MainWindow", "Space"))
        self.actionPause.setText(_translate("MainWindow", "Pause"))
        self.actionPause.setShortcut(_translate("MainWindow", "Shift+Space"))
        self.actionStop.setText(_translate("MainWindow", "Clear"))
        self.actionStop.setShortcut(_translate("MainWindow", "Esc"))
        self.actionBackward.setText(_translate("MainWindow", "Backward"))
        self.actionBackward.setShortcut(_translate("MainWindow", "Left"))
        self.actionForward.setText(_translate("MainWindow", "Forward"))
        self.actionForward.setShortcut(_translate("MainWindow", "Right"))
        self.actionSave_as_pdf.setText(_translate("MainWindow", "Save as pdf"))
        self.actionSave_as_pdf.setShortcut(_translate("MainWindow", "Ctrl+S"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
