# # import numpy as np
# # import wavio
# # # Parameters
# # rate = 44100    # samples per second
# # T = 3           # sample duration (seconds)
# # f = 440.0       # sound frequency (Hz)
# # # Compute waveform samples
# # t = np.linspace(0, T, T*rate, endpoint=False)
# # x = np.sin(2*np.pi * f * t)
# # # Write the samples to a file
# # wavio.write("sine.wav", x, rate, sampwidth=3)

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
    """
    create a synthetic 'sine wave' wave file with frequency freq
    file fname has a length of about data_size * 2
    """
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
    print("may take a moment ...")
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

# # amp = []
# for i in range(50):
#     amp.append(1000 + i*1000)
# data size, file size will be about 2 times that
# duration is about 4 seconds for a data_size of 40000
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

# librosa.display.waveplot(y=samples, sr=sampling_rate)
frequency = []
fftphase = np.angle(scipy.fft.rfft(samples))
fft = abs(scipy.fft.rfft(samples))
freqs = np.fft.rfftfreq(len(fft), (1.0 / sampling_rate))

ffti = []


# x = 10 * 5
# y = int(5 * 2500)

# for i in range(x, y):
#     fft[i] *= 50

for i in range(50001):
    # if fft[i] < 20:
    #     fft[i] = 100
    # if fft[i] < 10:
    #     fft[i] = 80
    ffti.append(
        fft[i] * math.cos((fftphase[i])) + fft[i] *
        math.sin((fftphase[i])) * 1j
    )

s = scipy.fft.irfft(ffti)

s = np.array(s)


write("test.wav", sampling_rate, s)
p = pyqtgraph.plot(freqs[range(len(fft) // 2)],
                   fft[range(len(fft) // 2)], pen="b")
p.setBackground("w")
c = pyqtgraph.plot(time, samples, pen="b")
c.setBackground("w")
x = pyqtgraph.plot(time, s, pen="r")
x.setBackground("w")
