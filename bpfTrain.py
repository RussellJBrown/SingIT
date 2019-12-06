from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.signal as signal
import librosa
import librosa.display
import librosa.feature
import IPython.display as ipd
import os

n = 10
filtertrain = [[0.0]]*13

filtertrain[0] = signal.butter(n, [3000,4000], 'bandpass', fs=44100, output='sos')
filtertrain[1] = signal.butter(n, [4000,5000], 'bandpass', fs=44100, output='sos')
filtertrain[2] = signal.butter(n, [5000,6000], 'bandpass', fs=44100, output='sos')
filtertrain[3] = signal.butter(n, [6000,7000], 'bandpass', fs=44100, output='sos')
filtertrain[4] = signal.butter(n, [7000,8000], 'bandpass', fs=44100, output='sos')
filtertrain[5] = signal.butter(n, [8000,9000], 'bandpass', fs=44100, output='sos')
filtertrain[6] = signal.butter(n, [9000,10000], 'bandpass', fs=44100, output='sos')
filtertrain[7] = signal.butter(n, [10000,11000], 'bandpass', fs=44100, output='sos')
filtertrain[8] = signal.butter(n, [11000,12000], 'bandpass', fs=44100, output='sos')
filtertrain[9] = signal.butter(n, [12000,13000], 'bandpass', fs=44100, output='sos')
filtertrain[10] = signal.butter(n, [13000,14000], 'bandpass', fs=44100, output='sos')
filtertrain[11] = signal.butter(n, [14000,15000], 'bandpass', fs=44100, output='sos')
filtertrain[12] = signal.butter(n, 15000, 'highpass', fs=44100, output='sos')

heightVar = 0.375
distanceVar = 4000

# I'm assuming there's 90 songs per language. If that's not the case, change it.
songArray = [[]]*90

# Insert algorithm for loading song locations into songArray here.

occurenceMatrix = [[0]*len(filtertrain)]*90
for i in np.arange(len(songArray)):
    y, sr = librosa.load(songArray[i])
    for j in np.arange(len(filtertrain)):
        filtered = signal.sosfilt(filtertrain[j], y)
        ypeaks = signal.find_peaks(filtered, height=np.max(filtered)*heightVar, distance=distanceVar)
        occurenceMatrix[i][j] = len(ypeaks[0])
        
# The contents of occurenceMatrix should then be saved to a .txt file.