from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QMessageBox
from mixer import Ui_MainWindow
from components import inputimg
import sys
import cv2
import numpy as np
import os
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="History.log",
                    format='%(lineno)s - %(levelname)s - %(message)s',
                    filemode='w')
logger = logging.getLogger()


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
        self.ui.component1_type.addItem("Uniphase")
        self.ui.component1_type.addItem("Unimagnitude")
        self.ui.component2_type.clear()
        for i in range (9):
            self.enable[i].setEnabled(False)

        for i in range(len(self.images)):
            self.images[i].ui.histogram.hide()
            self.images[i].ui.roiBtn.hide()
            self.images[i].ui.menuBtn.hide()
            self.images[i].ui.roiPlot.hide()


        self.counter=-1
        self.counter2=-1
        self.data=[]
        self.paths=[]
        self.imgwidth=[]
        self.imgheight=[]
        self.ui.actionOpen1.triggered.connect(lambda:self.opensignal(0))
        self.ui.actionOpen2.triggered.connect(lambda:self.opensignal(1))
        self.ui.img1_combo.currentTextChanged.connect(lambda:self.Components(0))
        self.ui.img2_combo.currentTextChanged.connect(lambda:self.Components(1))
        self.ui.output_channel.currentTextChanged.connect(lambda:self.mixer(0,False))
        self.ui.component2_type.currentTextChanged.connect(lambda:self.mixer(0,False))
        self.ui.component1_type.currentTextChanged.connect(lambda:self.mixer(1,True))
        self.ui.component1_img.currentTextChanged.connect(lambda:self.mixer(0,False))
        self.ui.component2_img.currentTextChanged.connect(lambda:self.mixer(0,False))
        self.ui.component1_slider.valueChanged.connect(lambda:self.mixer(0,False))
        self.ui.component2_slider.valueChanged.connect(lambda:self.mixer(0,False))


        # for i in range(0,2):
        #     self.sliders[i].valueChanged.connect(lambda:self.mixer())
        #     # self.types[i].currentTextChanged.connect(lambda:self.mixer())
        #     self.opimg[i].currentTextChanged.connect(lambda:self.mixer()) 

    def readsignal(self):
        logger.info("Browsing image ...")
        self.fname=QtGui.QFileDialog.getOpenFileName(self,' Open File',os.getenv('home'),"jpg(*.jpg) ;; jpeg(*.jpeg) ")
        self.path=self.fname[0]
        self.imgdata = inputimg(self.path)
        self.img= cv2.imread(self.path,0)
        self.height, self.width = self.img.shape
        if (self.path == True):
            logger.warning(" No image to open ")
        else:
            logger.info(" Browsed Successfully ! ")

    def opensignal(self ,num):
        if num == 0:
            self.readsignal()
            self.paths.append(self.path)
            self.imgwidth.append(self.width)
            self.imgheight.append(self.height)
            self.ui.img1_combo.setEnabled(True)
            self.ui.images[0].setImage((self.imgdata.img).T)
            self.ui.images[0].view.setAspectLocked(False)
            logger.info("Opened First image ...")
        if num == 1:
            self.readsignal()
            if self.width != self.imgwidth[0] or self.height !=self.imgheight[0]:
                QMessageBox.about(self,"Error !","Please Choose Another image with the same dimensions")
                logger.warning("Opened Image with different dimensions ...")
            else :
                self.paths.append(self.path)
                self.imgwidth.append(self.width)
                self.imgheight.append(self.height)
                self.ui.images[1].setImage((self.imgdata.img).T)
                self.ui.images[1].view.setAspectLocked(False)
                for i in range (9):
                    self.enable[i].setEnabled(True)
                    logger.info(" Opening Second image ...")
                    

    def Components(self,y):
        self.images[2+y%2].clear()
        self.path = self.paths[y%2]
        self.imgdata = inputimg(self.path)
        for i in range (0,y+1):
            if self.img_combo[i].currentText() == "Magnitude":
                x= self.imgdata.magnitude
                logger.info(" Presenting Magnitude.... ")
            elif self.img_combo[i].currentText() == "Phase":
                x= self.imgdata.phaseshift
                logger.info(" Presenting Phase.... ")
            elif self.img_combo[i].currentText() == "Real":
                x= self.imgdata.realshift
                logger.info(" Presenting Real.... ")
            elif self.img_combo[i].currentText() == "Imaginary": 
                x= self.imgdata.imaginaryshift
                logger.info(" Presenting Imaginary.... ")
            else: self.images[2+y%2].clear()
        self.images[2+y%2].setImage(x.T)
        self.images[2+y%2].view.setAspectLocked(False)
        # for i in range (0,y+1):
        #     n=self.img_combo[i].currentText().lower()
        #     x=self.imgdata.n
        # self.images[2+y%2].view.setRange(xRange=[0,self.imgheight[y%2]], yRange=[0,self.imgwidth[y%2]],padding=0)


    def mixer(self,z,flag):

        gain1=self.ui.component1_slider.value()
        gain2=self.ui.component2_slider.value()
        type1=self.types[0].currentText()
        type2= self.ui.component2_type.currentText()
        type22= self.ui.component2_type.currentText()
        self.img1=self.opimg[0].currentText()
        self.img2=self.opimg[1].currentText()
        opchannel=self.ui.output_channel.currentText()

        if (flag):
            self.setcombotext(type1,type22)



        if (self.img1 != self.img2):
        
            self.path1= self.paths[0]
            self.path2= self.paths[1]
            self.imgmix1= inputimg(self.path1)
            self.imgmix2= inputimg(self.path2)
            if (type1=="Magnitude" and type2=="Phase") or (type2=="Magnitude" and type1=="Phase" ):
                mode ="magphase"
            elif(type1=="Real" or type1=="Imaginary") and (type2=="Real" or type2=="Imaginary"):
                mode = "realimg"
            elif(type1=="Unimagnitude" and type2=="Phase" ) or (type2=="Unimagnitude" and type1=="Phase"):
                mode = "unimag"
            elif(type1=="Uniphase" and type2=="Magnitude") or (type2=="Uniphase" and type1=="Magnitude"):
                mode = "uniphase"
            elif(type1=="Uniphase" and type2=="Unimagnitude") or (type2=="Uniphase" and type1=="Unimagnitude"):
                mode = "uniuni"
            else: 
                logger.info("Error! Can't Mix ... ")
            
            try:
                if (self.img1 == "Image 1" and self.img2 == "Image 2" ):
                    output= self.imgmix1.mix(self.imgmix2,gain1,gain2,mode,type1,type2)
                else: 
                    output= self.imgmix2.mix(self.imgmix1,gain1,gain2,mode,type1,type2)
            except :
                pass


        try:
            if self.ui.output_channel.currentText() == "Output 1":        
                self.images[4].setImage((output).T)   
             
            elif self.ui.output_channel.currentText() == "Output 2":  
                self.images[5].setImage((output).T)
        except:
            pass

        # self.output(output)
        if (self.img1 == "Image 1" and self.img2 == "Image 1"):
            # logger.warning("Mixing the same image! , Dosen't affect the image")
            self.path1= self.paths[0]
            output= inputimg(self.path1).img

        elif(self.img1 == "Image 2" and self.img2 == "Image 2"):
            # logger.warning("Mixing the same image! , Dosen't affect the image")
            self.path1= self.paths[1]
            output= inputimg(self.path1).img

        try:

            logger.info(f"Mixing {gain1}% of {self.img1} {type1} and {gain2}% of {self.img2} {type2} in {self.ui.output_channel.currentText()} at mixing mood of: {mode} ")

        except: 
            pass


    def setcombotext(self, type1, type2):
    # def setcombotext(self, type1, type2):

        self.ui.component2_type.clear()

        if (type1 == "Magnitude" or type1 =="Unimagnitude"):
            self.ui.component2_type.addItem("Phase")
            self.ui.component2_type.addItem("Uniphase")
            self.ui.component2_type.setCurrentText("Phase")
        elif (type1 == "Phase" or type1== "Uniphase"):
            self.ui.component2_type.addItem("Magnitude")
            self.ui.component2_type.addItem("Unimagnitude")
            self.ui.component2_type.setCurrentText("Magnitude")
        elif type1 == "Real":
            self.ui.component2_type.addItem("Imaginary")
            self.ui.component2_type.setCurrentText("Imaginary")
        elif type1 == "Imaginary":
            self.ui.component2_type.addItem("Real")
            self.ui.component2_type.setCurrentText("Real")


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()
