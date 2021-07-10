from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow
from mainwindow import Ui_MainWindow 
import pickle
import sys
import os
import numpy as np
from UtilityClasses import FileBrowser
from AudioHandler import AudioHandler


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.simLabels = [self.ui.simLabel1, self.ui.simLabel2, self.ui.simLabel3, self.ui.simLabel4, self.ui.simLabel5, self.ui.simLabel6, self.ui.simLabel7]       
        self.songHandler = None
        self.secSongHandler = None
        self.mixedSong = None
        
        self.handleMixerBox('off')
        
        self.ui.mixerDisableButton.pressed.connect(lambda: self.handleMixerBox('off'))
        self.ui.mixerEnableButton.pressed.connect(lambda: self.handleMixerBox('on'))
        self.ui.resetButton.pressed.connect(self.reset)                
        self.ui.menuLoadSong.triggered.connect(self.getFile)       
        self.ui.recognizeButton.pressed.connect(self.recongizeSong)
        self.ui.weightSlider.valueChanged.connect(self.updateMixerUI)
        
        
    def getFile(self):
        fileBrowser = FileBrowser()
        path = fileBrowser.getFilePath()
        self.handleFile(path)        
        
    def handleFile(self, path):
        if(self.songHandler == None):
            self.songHandler = AudioHandler(path)
            self.songHandler.initalize()
            self.updateSongUI()
        else:
            self.secSongHandler = AudioHandler(path)
            self.secSongHandler.initalize()
            self.updateMixerUI()
        
    def updateSongUI(self):
        if(self.songHandler == None):
            self.ui.songLabel.setText('N/A')
            self.ui.srLabel.setText('N/A')
            return
                      
        self.ui.songLabel.setText(self.songHandler.getSongName())
        self.ui.srLabel.setText('44.1 KHz')
        
    def updateSimilarityUI(self, sortedSimilarity):
        if(sortedSimilarity == None):
            for label in self.simLabels:
                label.setText('N/A')
            return
            
        counter = 0     
        for label in self.simLabels:
            label.setText(sortedSimilarity[counter][0] + ': ' + str(sortedSimilarity[counter][1]))
            counter += 1
        
    def updateMixerUI(self):
        if(self.secSongHandler == None):
            self.ui.songLabel2.setText('N/A')
            self.ui.srLabel2.setText('N/A')
            return
        
        self.ui.songLabel2.setText(self.secSongHandler.getSongName())
        self.ui.srLabel2.setText('44100')
        
        weight = self.ui.weightSlider.value() / 10.0
        
        self.mixedSong = self.songHandler.mix(self.secSongHandler, weight)
        self.mixedSong.initSongData()
        self.mixedSong.initRolloffFreq()
        self.mixedSong.initSpectrogram()
        self.mixedSong.saveSpectrogram()
        self.mixedSong.saveRolloffFreq()
        self.mixedSong.getSpectrogramHash()
        self.mixedSong.getRolloffFreqHash()
        self.recognizeMix()
        
    def recognizeMix(self):
        sortedSimilarity = self.mixedSong.compareHash()
        self.updateSimilarityUI(sortedSimilarity)
        self.ui.recognizeButton.setEnabled(False)
        
    def recongizeSong(self):
        if(self.songHandler == None):
            self.updateSimilarityUI(None)
            return
        
        sortedSimilarity = self.songHandler.compareHash()
        self.updateSimilarityUI(sortedSimilarity)          
    
    def handleMixerBox(self, cmd):
        if cmd == 'off':
            self.ui.mixerBox.setEnabled(False)
            self.updateSongUI()
            self.updateSimilarityUI(None)
        elif cmd == 'on':
            if(self.songHandler != None):
                self.ui.mixerBox.setEnabled(True)
        else:
            pass
    
    def reset(self):
        self.songHandler = None
        self.secSongHandler = None
        self.mixedSong = None
        self.ui.recognizeButton.setEnabled(True)
        self.updateSongUI()
        self.updateSimilarityUI(None)
        self.updateMixerUI()
        self.handleMixerBox('off')            
        
if __name__ == '__main__':
       
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()