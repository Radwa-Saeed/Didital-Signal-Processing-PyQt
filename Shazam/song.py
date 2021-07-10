import numpy as np
import librosa
import librosa.display
from librosa.core import load
import hashlib
from pydub import AudioSegment
import tempfile
from PIL import Image
import imagehash
import pylab
import os
import soundfile as sf

class song():

    def __init__(self, Path: str):

        self.path=Path
        musicdata = AudioSegment.from_mp3(self.path)[0:60000]
        wavdata=tempfile.mktemp ('.wav')
        musicdata.export(wavdata, format="wav")
        self.data, self.fs= librosa.load(wavdata)



    def loaddata(self):
        return self.data

    def loadfs(self):
        return self.fs

    def spectro(self):
        self.stft = np.abs(librosa.stft(self.data))
        self.spectro = librosa.amplitude_to_db(self.stft)
        librosa.display.specshow(self.spectro, y_axis='linear')
        pylab.savefig('spectros/spec.'+ os.path.splitext(os.path.basename(self.path))[0] + '.png', bbox_inches=None, pad_inches=0)
        pylab.close()


    def getSongName(self):
        baseFileName = os.path.basename(self.path)
        songName = os.path.splitext(baseFileName)[0]
        return songName  

    def hashdata(self, datatohash):
        self.newimage=Image.fromarray(datatohash)
        self.hashed=imagehash.phash(self.newimage, hash_size=16)
        return self.hashed

    def feature1(self):

        self.melSpectrogram = librosa.feature.melspectrogram(y= self.data, sr = self.fs)
        self.hashedmelspec = self.hashdata(self.melSpectrogram)
 
        return self.hashedmelspec

    def feature2(self):

        self.chroma = librosa.feature.chroma_stft(y=self.data, sr=self.fs)
        self.hashedchroma = self.hashdata(self.chroma)
        return self.hashedchroma


    def feature3(self):

        self.mcff = librosa.feature.mfcc(y=self.data, sr=self.fs, n_mfcc=13)
        self.hashedmcff = self.hashdata(self.mcff)
        return self.hashedmcff



    def feature4(self):

        self.spectralcent = librosa.feature.spectral_centroid(y=self.data, sr=self.fs)
        self.hashedspectral = self.hashdata(self.spectralcent)
        return self.hashedspectral



    def feature5(self): 

        self.rolloffFreq = librosa.feature.spectral_rolloff(y= self.data, sr = self.fs)[0]
        self.hashedrollof = self.hashdata(self.rolloffFreq)
        return self.hashedrollof


    def mix(self, songtomix: 'song', slider):
        self.outputSong = (self.data * slider) + ( (songtomix.loaddata()) * (1 - slider))
        path = 'Database'+ 'mixed.wav'
        sf.write(path, self.outputSong, 22050)
        self.mixedSong = song(path)
        print (len(self.data))
        print (len(songtomix.loaddata()))
        print (len(self.outputSong))
        return self.mixedSong