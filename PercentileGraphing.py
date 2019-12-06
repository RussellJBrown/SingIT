import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal 
from scipy.interpolate import interp1d 
import IPython.display as ipd
import scipy.io.wavfile as wav

import librosa
import sklearn

target = np.append(["English"]*90,["French"]*90)
target = np.append(target,["Japanese"]*90)
target = np.append(target,["German"]*90)

EnglishPks = np.array([[0]*13]*90)
FrenchPks = np.array([[0]*13]*90)
JapanesePks = np.array([[0]*13]*90)
GermanPks = np.array([[0]*13]*90)

with open("EnglishPeaks30.txt",'r') as file:
    data = file.read().replace('\n', ' ')
    data = data.replace('  ',' ')
    data = data.split()
    for i in np.arange(90):
        for j in np.arange(13):
            EnglishPks[i][j] = int(data[i*13+j])
with open("FrenchPeaks30.txt",'r') as file:
    data = file.read().replace('\n', ' ')
    data = data.replace('  ',' ')
    data = data.split()
    for i in np.arange(90):
        for j in np.arange(13):
            FrenchPks[i][j] = int(data[i*13+j])
with open("JapanesePeaks30.txt",'r') as file:
    data = file.read().replace('\n', ' ')
    data = data.replace('  ',' ')
    data = data.split()
    for i in np.arange(90):
        for j in np.arange(13):
            JapanesePks[i][j] = int(data[i*13+j])
with open("GermanPeaks30.txt",'r') as file:
    data = file.read().replace('\n', ' ')
    data = data.replace('  ',' ')
    data = data.split()
    for i in np.arange(90):
        for j in np.arange(13):
            GermanPks[i][j] = int(data[i*13+j])

allPks = np.append(np.append(EnglishPks,FrenchPks,axis=0),np.append(JapanesePks,GermanPks,axis=0),axis=0)

English13 = [0]*90
French13 = [0]*90
Japanese13 = [0]*90
German13 = [0]*90

# Change this number to analyze different bands.
bandnum = 13

for i in np.arange(90):
    English13[i] = EnglishPks[i][bandnum-1]
    French13[i] = FrenchPks[i][bandnum-1]
    Japanese13[i] = JapanesePks[i][bandnum-1]
    German13[i] = GermanPks[i][bandnum-1]

English13 = np.sort(English13)
French13 = np.sort(French13)
Japanese13 = np.sort(Japanese13)
German13 = np.sort(German13)

EnglishTarget = [4]*90
FrenchTarget = [3]*90
JapaneseTarget = [2]*90
GermanTarget = [1]*90
yaxis90 = np.arange(90)+1

plt.scatter(English13,yaxis90)
plt.scatter(French13,yaxis90)
plt.scatter(Japanese13,yaxis90)
plt.scatter(German13,yaxis90)
