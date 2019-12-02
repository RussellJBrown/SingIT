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

bands = np.array([[[0]*90]*4]*13)

for i in np.arange(13):
    for j in np.arange(90):
        bands[i][0][j] = EnglishPks[j][i]
        bands[i][1][j] = FrenchPks[j][i]
        bands[i][2][j] = JapanesePks[j][i]
        bands[i][3][j] = GermanPks[j][i]
    for j in np.arange(4):
        bands[i][j] = np.sort(bands[i][j])
    
def findPercentile(bnum, lnum, index):
    locs = np.where(bands[bnum][lnum]==index)[0]
    if len(locs) > 0:
        return int(np.max(locs)+1)
    elif index == 0:
        return 0
    else:
        return findPercentile(bnum,lnum,index-1)

def predictor(arr, printMatrix, printPredictions):
    if len(arr) < 13:
        print("Incompatible array size.")
    else:
        bmatrix = np.array([[0]*4]*13)
        for i in np.arange(13):
            for j in np.arange(4):
                outof90 = int(findPercentile(i, j, arr[i]))
                #print(type(outof90))
                bmatrix[i][j] = abs(outof90 - int(90 - outof90))
    bmatrix = bmatrix//2
    predictions = np.array([0]*4)
    for i in np.arange(13):
        for j in np.arange(4):
            predictions[j] = predictions[j] + bmatrix[i][j]
    print("This was predicted as:")
    if predictions[0] == np.min(predictions):
        print("\tEnglish")
    if predictions[1] == np.min(predictions):
        print("\tFrench")
    if predictions[2] == np.min(predictions):
        print("\tJapanese")
    if predictions[3] == np.min(predictions):
        print("\tGerman")
    if printMatrix > 0:
        print(bmatrix)
    if printPredictions > 0:
        print(predictions)
        
EnglishSums = np.array([2531, 1894, 1942, 1816, 1638, 1510, 1211, 1050, 1069, 1110, 1017, 1100, 1420])/90
FrenchSums = np.array([2233, 1830, 2065, 1753, 1698, 1364, 1150, 1130, 1104, 1022, 1131, 1199, 1494])/90
GermanSums = np.array([2318, 1899, 1898, 1693, 1587, 1395, 1265, 1312, 1359, 1464, 1565, 1628, 2200])/90
JapaneseSums = np.array([2546, 2021, 1838, 1886, 2132, 1930, 1454, 1056, 866, 815, 864, 897, 1163])/90
xaxis13 = np.arange(13)+1

# inputarr is where you put the numbers you want to test for a single song.
inputarr = np.array([45, 50, 28, 18, 13, 9, 11, 17, 15, 18, 31, 30, 50])

predictor(inputarr,0,1)

plt.scatter(xaxis13,EnglishSums) # Blue
plt.scatter(xaxis13,FrenchSums) # Orange
plt.scatter(xaxis13,JapaneseSums) # Green
plt.scatter(xaxis13,GermanSums) # Red
plt.scatter(xaxis13,inputarr) # Purple
