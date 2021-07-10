import librosa
from song import song
import song as sg
import os
import os
from PIL import Image
import imagehash
from pydub import AudioSegment
import csv


writer = csv.writer(open('hashdata.csv', 'w', newline=''))
writer.writerow(["Name" , "melSpectrogram", "chroma", "mcff", "spectralcent", "rolloffFreq"])

directory = r'Database'    
for song in os.listdir(directory):
    
    if song.endswith(".mp3"):
        path = os.path.join(directory, song)
        songdata = sg.song(path)
        songdata.spectro()
        feat1=songdata.feature1()
        feat2=songdata.feature2()
        feat3=songdata.feature3()
        feat4=songdata.feature4()
        feat5=songdata.feature5() 
        writer.writerow([song, feat1, feat2, feat3, feat4, feat5])

        # print(feat1)
