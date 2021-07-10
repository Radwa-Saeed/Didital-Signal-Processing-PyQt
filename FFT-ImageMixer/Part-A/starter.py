from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QMessageBox
from mixer import Ui_MainWindow
from components import inputimg
import sys
import cv2
import numpy as np
import os
class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.images=[self.ui.img1,self.ui.img2,self.ui.img1_component,self.ui.img2_component,self.ui.output1,self.ui.output2]
        self.img_combo=[self.ui.img1_combo,self.ui.img2_combo]
        self.sliders=[self.ui.component1_slider, self.ui.component2_slider]
        self.types=[self.ui.component1_type,self.ui.component2_type]
        self.opimg=[self.ui.component1_img,self.ui.component2_img]
        self.enable=[self.ui.output_channel, self.ui.component1_img,self.ui.component2_img, self.ui.component1_type, self.ui.component2_type, self.ui.component1_slider, self.ui.component2_slider, self.ui.img1_combo,  self.ui.img2_combo]
        for i in range (9):
            self.enable[i].setEnabled(False)
        # self.images=[self.ui.img2,self.ui.img1_component,self.ui.img2_component,self.ui.output1,self.ui.output2]
        for i in range(len(self.images)):
            self.images[i].ui.histogram.hide()
            self.images[i].ui.roiBtn.hide()
            self.images[i].ui.menuBtn.hide()
            self.images[i].ui.roiPlot.hide()
        self.counter=-1
        self.data=[]
        self.paths=[]
        self.imgwidth=[]
        self.imgheight=[]
        self.ui.actionOpen1.triggered.connect(lambda:self.opensignal(0))
        self.ui.actionOpen2.triggered.connect(lambda:self.opensignal(1))
        self.ui.img1_combo.currentTextChanged.connect(lambda:self.Components(0))
        self.ui.img2_combo.currentTextChanged.connect(lambda:self.Components(1))
        self.ui.output_channel.currentTextChanged.connect(lambda:self.mixer())
        
        for i in range(0,2):
            self.sliders[i].valueChanged.connect(lambda:self.mixer())
            self.types[i].currentTextChanged.connect(lambda:self.mixer())
            self.opimg[i].currentTextChanged.connect(lambda:self.mixer())
        
    def readsignal(self):
        self.fname=QtGui.QFileDialog.getOpenFileName(self,' Open File',os.getenv('home'),"jpg(*.jpg) ;; jpeg(*.jpeg) ")
        self.path=self.fname[0]
        self.imgdata = inputimg(self.path)
        self.img= cv2.imread(self.path,0)
        self.height, self.width = self.img.shape
        if (self.path): 
            pass
        
    def opensignal(self ,num):
        if num == 0:
            self.readsignal()
            self.paths.append(self.path)
            self.imgwidth.append(self.width)
            self.imgheight.append(self.height)
            self.ui.img1_combo.setEnabled(True)
            #print(self.imgwidth , self.imgheight)
            self.ui.images[0].setImage((self.imgdata.img).T)
            #self.ui.images[0].view.setRange(xRange=[0,self.width], yRange=[0,self.height],padding=0)
        if num == 1:
            self.readsignal()
            if self.width != self.imgwidth[0] or self.height !=self.imgheight[0]:
                QMessageBox.about(self,"Error !","Please Choose Another image with the same dimensions")
            else :
                self.paths.append(self.path)
                self.imgwidth.append(self.width)
                self.imgheight.append(self.height)
                self.ui.images[1].setImage((self.imgdata.img).T)
                for i in range (9):
                    self.enable[i].setEnabled(True)
                #self.ui.images[1].view.setRange(xRange=[0,self.width], yRange=[0,self.height],padding=0)   
                    
    def Components(self,y):
        self.images[2+y%2].clear()
        # if y==0 :
        #     self.path=self.paths[0]
        # else: 
        #     self.path= self.paths[1]
        self.path = self.paths[y%2]
        self.imgdata = inputimg(self.path)
        for i in range (0,y+1):
            if self.img_combo[i].currentText() == "Magnitude":
                x= self.imgdata.magnitude
                print(self.img_combo[i].currentText())
                print(y)
            elif self.img_combo[i].currentText() == "Phase":
                x= self.imgdata.phaseshift
                print(self.img_combo[i].currentText())
                print(y)
            elif self.img_combo[i].currentText() == "Real":
                x= self.imgdata.realshift
                print(self.img_combo[i].currentText())
                print(y)
            elif self.img_combo[i].currentText() == "Imaginary": 
                x= self.imgdata.imaginaryshift
                print(self.img_combo[i].currentText())
                print(y)
            else: self.images[2+y%2].clear()
        self.images[2+y%2].setImage(x.T)
        self.images[2+y%2].view.setRange(xRange=[0,self.imgheight[y%2]], yRange=[0,self.imgwidth[y%2]],padding=0)
    def mixer(self):
        self.gain1=self.ui.component1_slider.value()
        self.gain2=self.ui.component2_slider.value()
        self.type1=self.types[0].currentText()
        self.type2=self.types[1].currentText()
        self.img1=self.opimg[0].currentText()
        self.img2=self.opimg[1].currentText()
        if (self.img1 != self.img2):
            self.path1= self.paths[0]
            self.path2= self.paths[1]
            self.imgmix1= inputimg(self.path1)
            self.imgmix2= inputimg(self.path2)
            if (self.type1=="Magnitude" or self.type1=="Phase") and (self.type2=="Magnitude" or self.type2=="Phase"):
                self.mode ="magphase"
                print ("check1")
                print (self.type1, self.type2)
                print( self.img1, self.img2)
            elif(self.type1=="Real" or self.type1=="Imaginary") and (self.type2=="Real" or self.type2=="Imaginary"):
                self.mode = "realimg"
                print (self.type1, self.type2)
                print( self.img1, self.img2)
                print ("check2")
            else: 
                self.mode ="other"
                print("can't mix")
                print (self.type1, self.type2)
                print( self.img1, self.img2)
            
            if (self.img1 == "Image 1" and self.img2 == "Image 2" ):
                output= self.imgmix1.mix(self.imgmix2,self.gain1,self.gain2,self.mode,self.type1,self.type2)
                print ("check3")
            else: 
                output= self.imgmix2.mix(self.imgmix1,self.gain1,self.gain2,self.mode,self.type1,self.type2)
                print ("check4", "\n")
        elif (self.img1 == "Image 1" and self.img2 == "Image 1"):
            self.path1= self.paths[0]
            output= inputimg(self.path1).img
        elif(self.img1 == "Image 2" and self.img2 == "Image 2"):
            self.path1= self.paths[1]
            output= inputimg(self.path1).img
        else: 
            print (self.type1, self.type2)
            print( self.img1, self.img2)
            print (" Unexpected error")
            #show the same image ba3deen
        if self.ui.output_channel.currentText() == "Output 1":        
            self.images[4].setImage((output).T)    
        elif self.ui.output_channel.currentText() == "Output 2":  
            # self.ui.component1_type.setItemText(0)
            self.images[5].setImage((output).T)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()