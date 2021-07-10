from re import search
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from numpy.core.numeric import count_nonzero
from app import Ui_MainWindow
import sys , os
import librosa
import os
import librosa.display
from librosa.core import load
from pydub import AudioSegment
from tempfile import mktemp # To convert mp3 to wav
import pylab
import numpy as np
import matplotlib.pyplot as plt
from song import *
import pandas as pd
from difflib import SequenceMatcher
from PyQt5.QtWidgets import QMessageBox
from imagehash import hex_to_hash
data = pd.read_csv('hashdata.csv')

songfeats=[0,0,0,0]

diffvalue=[0,0,0,0]

# self.results=[]

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.DisableMixer()
        self.ui.File1_Browse.clicked.connect(lambda:self.readsignal(0))
        self.ui.File2_Browse.clicked.connect(lambda:self.readsignal(1))        
        self.ui.Search.clicked.connect(lambda:self.similarity())
        self.ui.mixer.valueChanged.connect(self.mixer)
        self.ui.mixer.setTracking(False)
        self.ui.mixer.setMaximum(100)
        self.ui.mixer.setMinimum(0)
        self.ui.mixer.setSingleStep(1)
        self.ui.mixer.setValue(0)        
        self.results=[]
        newfeats=[]
        self.paths=[None,None]
    
    def readsignal(self,songnum):
        self.fname=QtWidgets.QFileDialog.getOpenFileName(self,' Open File',os.getenv('home'),"mp3(*.mp3) ;; wav(*.wav)")
        self.path=self.fname[0]        
        if songnum ==0 :
            print(self.results)
            self.paths[0]=self.path
            self.ui.name_song1.setText(os.path.splitext(os.path.basename(self.path))[0]) #to write song name
            self.song1 = song(self.path)
            hashedd= self.song1.feature1()
            print(hashedd)
            print(self.song1.loadfs())
            print("file1 read done")
        elif songnum ==1 :    
            print(self.results)        
            self.paths[1]=self.path
            self.ui.name_song2.setText(os.path.splitext(os.path.basename(self.path))[0])
            self.EnableMixer()
            self.song2 = song(self.path)
            hashedd= self.song2.feature1()
            print(self.song2.loadfs())
            print(hashedd)
            print("file2 read done")

    def DisableMixer(self):
        self.ui.mixer.setEnabled(False)

    def EnableMixer(self):
        self.ui.mixer.setEnabled(True)

    def mixer(self) :
        self.slider = self.ui.mixer.value()/100
        self.path1= self.paths[0]
        self.path2= self.paths[1]
        self.song11= song(self.path1)
        self.song22= song(self.path2)
        self.mixedsong= self.song11.mix(self.song22, self.slider)
        mixfeat1= self.mixedsong.feature1()
        # print(type(mixfeat1))
        print(mixfeat1)

    def hammingcheck(self,s1,s2):
         return hex_to_hash(s1) - hex_to_hash(s2)


    def findsimilarto(self,feat1, feat2, feat3):
        self.results=[]
        newfeats=[0,feat1, feat2, feat3]
        for i in range(len(data)):
            songname2=data.iloc[i,0]
            for j in range(1,4):
                songfeats[j]=data.iloc[i,j]
                diffvalue[j]=( 1-(imagehash.hex_to_hash(str(newfeats[j]))- imagehash.hex_to_hash(str(songfeats[j])) ) / 256.0 )
            print(newfeats)
            print(songfeats)
            similarity= (diffvalue[1]+diffvalue[2]+diffvalue[3])/0.03
            self.results.append((songname2,(similarity)))
        self.results.sort(key= lambda x: x[1], reverse=True)    
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setRowCount(10)
        for i in range(10):
            self.ui.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(self.results[i][0]))
            self.ui.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(str((self.results[i][1]))+"%"))      

    def similarity(self):
        if (self.paths[0] is not None) & (self.paths[1] is not None):
            self.slider = self.ui.mixer.value()/100
            self.song11= song(self.paths[0])
            self.song22= song(self.paths[1])
            self.mixedsong= self.song11.mix(self.song22, self.slider)
            self.findsimilarto(self.mixedsong.feature1(),self.mixedsong.feature2(),self.mixedsong.feature3())
        elif (self.paths[0] is not None):
            self.thissong1=song(self.paths[0])
            self.findsimilarto(self.thissong1.feature1(),self.thissong1.feature2(),self.thissong1.feature3())
        elif (self.paths[1] is not None):
            self.thissong2=song(self.paths[1])
            self.findsimilarto(self.thissong2.feature1(), self.thissong2.feature2(), self.thissong2.feature3())
        else:
            print("no songs")   

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()
