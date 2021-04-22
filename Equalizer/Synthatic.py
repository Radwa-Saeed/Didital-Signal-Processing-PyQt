
import math
import wave
import struct
import librosa
import matplotlib.pyplot as plt
from librosa import display
import numpy as np
import scipy.fftpack
import pyqtgraph
from scipy.io.wavfile import write


def make_soundfile(freq, data_size, fname="test.wav"):

    frate = 11025.0  # framerate as a float
    amp = 8000.0  # multiplier for amplitude

    # make a sine list ...
    sine_list = []
    for x in range(data_size):
        index = int(x / 364)
        sine_list.append(math.sin(2 * math.pi * freq[index] * (x / frate)))

    # get ready for the wave file to be saved ...
    wav_file = wave.open(fname, "w")
    # give required parameters
    nchannels = 1
    sampwidth = 2
    framerate = int(frate)
    nframes = data_size
    comptype = "NONE"
    compname = "not compressed"
    # set all the parameters at once
    wav_file.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))
    # now write out the file ...
    print("may take a moment ...")
    for s in sine_list:
        # write the audio frames to file
        wav_file.writeframes(struct.pack("h", int(s * amp / 2)))

    wav_file.close()
    print("%s written" % fname)


def soundfile(samples):
    wav_file = wave.open("test.wav", "w")
    # give required parameters
    frate = sampling_rate
    nchannels = 1
    sampwidth = 2
    framerate = int(frate)
    nframes = data_size
    comptype = "NONE"
    compname = "not compressed"
    # set all the parameters at once
    wav_file.setparams((nchannels, sampwidth, framerate,
                        nframes, comptype, compname))
    # now write out the file ...
    for s in samples:
        # write the audio frames to file
        wav_file.writeframes(struct.pack("h", int(s * 8000 / 2)))

    wav_file.close()
    print("%s written" % fname)


# set some variables ...
freq = []
for i in range(10, 5500, 20):
    # freq = [100, 200, 300, 600, 1000, 1500, 5000, 6000, 6500, 7500]
    freq.append(i)
print(len(freq))

data_size = 100000

# write the synthetic wave file to ...
fname = "WaveTest2.wav"


make_soundfile(freq, data_size, fname)

file_path = "WaveTest2.wav"
samples, sampling_rate = librosa.load(
    file_path, sr=None, mono=True, offset=0.0, duration=None
)

duration = len(samples) / sampling_rate
time = np.arange(0, duration, 1 / sampling_rate)
