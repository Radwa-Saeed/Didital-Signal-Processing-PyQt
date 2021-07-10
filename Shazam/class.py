import pylab
import os
import numpy as np
import librosa
import imagehash
from PIL import Image
import operator
import pickle
import soundfile as sf
import matplotlib.pyplot as plt
import librosa.display

# TODO:
#   - implement protected variables?
#   - rectify similarity index value *IMPORTANT*
#   - increase similarity search effectiveness with feature comparison *IMPORANT*
#   - add mixer functionality *IMPORTANT*


class AudioHandler():
    def __init__(self, songPath):        
        self.songPath = songPath
        self.songName = self.getSongName()
        self.songData = None
        self.melSpectrogram = None
        self.spectrogramHash = None
        self.rolloffFreq = None
        self.rolloffFreqHash = None
        self.simIndex = {}
                
    def initSongData(self):
        if(self.songData != None):
            return
        
        self.songData, sr = librosa.load(self.songPath, sr = 44100, duration = 60)
        return self.songData
    
    def initSpectrogram(self):
        if(self.melSpectrogram != None):
            return
        
        self.melSpectrogram = librosa.feature.melspectrogram(self.songData, sr = 44100)
        self.logSpectrogram = librosa.power_to_db(self.melSpectrogram, ref = np.max)
        return self.melSpectrogram
    
    def initRolloffFreq(self):
        if(self.rolloffFreq != None):
            return
        
        self.rolloffFreq = librosa.feature.spectral_rolloff(self.songData+0.01, sr=44100)[0]
    
    def saveSpectrogram(self):
        save_path = 'Database/Spectrograms/' + self.songName + '.jpg'
        
        plt.ioff()
        pylab.axis('off') #Removes axes
        pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[]) #Removes white edges
        
        librosa.display.specshow(self.logSpectrogram, sr = 441000, x_axis='time', y_axis='mel')

        pylab.savefig(save_path, bbox_inches=None, pad_inches=0)
        pylab.close()
        
    def saveRolloffFreq(self):
        save_path = 'Database/Rolloff Frequencies/' + self.songName + '.jpg'
        
        pylab.axis('off') #Removes axes
        pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[]) #Removes white edges
        
        plt.ioff()
        plt.semilogy(self.rolloffFreq.T)
        
        pylab.savefig(save_path, bbox_inches=None, pad_inches=0)
        pylab.close()
        
    def getSpectrogramHash(self):
        self.spectrogramHash = imagehash.phash(Image.open('Database/Spectrograms/' + self.songName + '.jpg'))       
        return self.spectrogramHash
    
    def getRolloffFreqHash(self):
        self.rolloffFreqHash = imagehash.phash(Image.open('Database/Rolloff Frequencies/' + self.songName + '.jpg'))   
        return self.spectrogramHash
    
    def compareHash(self): #this function can be easily modified to handle a given database passed by an argument.
        with open('Database/Hash/specHashDatabase.pickle', 'rb') as handle:
            specHashDatabase = pickle.load(handle)
            
        with open('Database/Hash/rollHashDatabase.pickle', 'rb') as handle:
            rollHashDatabase = pickle.load(handle)
        
        for songName in specHashDatabase:
            self.simIndex[songName] = self.spectrogramHash - specHashDatabase[songName] 
        
        for songName in rollHashDatabase:
            self.simIndex[songName] = ((self.rolloffFreqHash - rollHashDatabase[songName]) + self.simIndex[songName]) / 2
            
        sorted_simIndex = sorted(self.simIndex.items(), key = operator.itemgetter(1))
            
        return sorted_simIndex
    
    def mix(self, secondSong: 'AudioHandler', weight):
        newSong = (self.songData * weight) + (secondSong.songData * (1 - weight))
        path = 'Database/Songs/Mixer/' + self.songName[:-3] + '+' + secondSong.songName[:-3] + '.wav'
        sf.write(path, newSong, 44100)
        
        mixedSong = AudioHandler(path)
        return mixedSong
                          
    def getSongName(self):
        baseFileName = os.path.basename(self.songPath)
        songName = os.path.splitext(baseFileName)[0]
        return songName        
        
    def getSongData(self):
        return self.songData
    
    def getSpectrogram(self):
        return self.melSpectrogram
    
    def initalize(self):
        self.initSongData()
        self.initSpectrogram()
        self.initRolloffFreq()
        self.getSpectrogramHash()
        self.getRolloffFreqHash()
    
