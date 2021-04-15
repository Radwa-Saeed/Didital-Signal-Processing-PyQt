# import numpy as np
# import wavio
# # Parameters
# rate = 44100    # samples per second
# T = 3           # sample duration (seconds)
# f = 440.0       # sound frequency (Hz)
# # Compute waveform samples
# t = np.linspace(0, T, T*rate, endpoint=False)
# x = np.sin(2*np.pi * f * t)
# # Write the samples to a file
# wavio.write("sine.wav", x, rate, sampwidth=3)

import math
import wave
import struct
import librosa
import matplotlib.pyplot as plt
from librosa import display
import numpy as np
import scipy.fftpack
import pyqtgraph


def make_soundfile(freq, data_size, fname="test.wav"):
    """
    create a synthetic 'sine wave' wave file with frequency freq
    file fname has a length of about data_size * 2
    """
    frate = 11025.0  # framerate as a float
    amp = 8000.0     # multiplier for amplitude

    # make a sine list ...
    sine_list = []
    for x in range(data_size):
        index = int(x/10000)
        sine_list.append(math.sin(2*math.pi*freq[index]*(x/frate)))

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
    wav_file.setparams((nchannels, sampwidth, framerate, nframes,
                        comptype, compname))
    # now write out the file ...
    print("may take a moment ...")
    for s in range(len(sine_list)):
        # write the audio frames to file
        wav_file.writeframes(struct.pack('h', int(sine_list[s]*amp/2)))
    wav_file.close()
    print("%s written" % fname)


# set some variables ...
freq =  [100, 200, 300, 600, 1000, 1500, 5000, 6000, 6500, 7500]
# for i in range(10, 10010, 20):
#         #freq = [100, 200, 300, 600, 1000, 1500, 5000, 6000, 6500, 7500]
#     freq.append(i)
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
    file_path, sr=None, mono=True, offset=0.0, duration=None)

# librosa.display.waveplot(y=samples, sr=sampling_rate)
frequency = []
fft = abs(scipy.fftpack.fft(samples))
freqs = np.fft.fftfreq(len(fft), (1.0/sampling_rate))
print(np.argmax(freqs[range(len(fft)//2)]))

pyqtgraph.plot(freqs[range(len(fft)//2)], fft[range(len(fft)//2)])
# # librosa.feature.melspectrogram(y=samples, sr=sampling_rate)
# D = librosa.amplitude_to_db(np.abs(librosa.stft(samples)), ref=np.max)
# # S = librosa.feature.melspectrogram(S=D, sr=sampling_rate)
# fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
# S_dB = librosa.power_to_db(S, ref=np.max)
# img = librosa.display.specshow(D, x_axis='time',
#                          y_axis='mel', sr=sampling_rate,
#                          fmax=8000, ax=ax)
# fig.colorbar(img, ax=ax, format='%+2.0f dB')
# ax.set(title='Mel-frequency spectrogram')
fig, ax = plt.subplots(nrows=4, ncols=1, sharex=True)
D = librosa.amplitude_to_db(np.abs(librosa.stft(samples)), ref=np.max)
img = librosa.display.specshow(D, y_axis='linear', x_axis='time',
                               sr=sampling_rate, ax=ax[0], cmap='BuGn')
hop_length = 1024
D = librosa.amplitude_to_db(np.abs(librosa.stft(samples, hop_length=hop_length)),
                            ref=np.max)
librosa.display.specshow(D, y_axis='log', sr=sampling_rate, hop_length=hop_length,
                         x_axis='time', ax=ax[1], cmap='gray')
librosa.display.specshow(D, y_axis='mel', sr=sampling_rate, hop_length=hop_length,
                         x_axis='time', ax=ax[2], cmap='inferno')
librosa.display.specshow(D, y_axis='cqt_hz', sr=sampling_rate, hop_length=hop_length,
                         x_axis='time', ax=ax[3])
ax[1].set(title='Log-frequency power spectrogram')
ax[2].set(title='Mel scale spectrogram')
ax[3].set(title='CQT spectrogram')
ax[1].label_outer()
ax[2].label_outer()
ax[0].set(title='Linear-frequency power spectrogram')
ax[0].label_outer()
fig.colorbar(img, ax=ax, format="%+2.f dB")
plt.show()