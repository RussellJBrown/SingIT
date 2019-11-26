from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
from collections import defaultdict
import itertools
import os

def to_str(var):
    return str(list(np.reshape(np.asarray(var), (1, np.size(var)))[0]))[1:-1]

#This method extracts 10 seconds of the song and outputs a new file
def libroExtract(inputSong,Language):
    name = os.path.splitext(inputSong)[0]
    extension = os.path.splitext(inputSong)[1]
    outSong = name + "Out" + extension
    outSong = outSong.replace("(","")
    outSong = outSong.replace(")","")
    outSong = outSong.replace("'","")
    outSong = outSong.replace('"','')
    outSong = outSong.replace(" ",'')
    y, sr = librosa.load(inputSong,offset=35.0,duration=10)
    librosa.output.write_wav(outSong,y,sr)
    #kClustering(outSong,Language)
    return outSong


def nextPhase(output,Language):
    fileNames = "Vocal"+Language+".txt"
    fileName3 = "MFCC"+Language+".txt"

    y, sr = librosa.load(output,duration=50)
    centralCentroid = librosa.feature.spectral_centroid(y=y,sr=sr)
    normalMean = np.mean(centralCentroid)
    normalSTD  = np.std(centralCentroid)

    f = open(fileNames,'a')
    f.write(to_str(normalMean))
    f.write(" ")
    f.write(to_str(normalSTD))
    f.write("\n")
    f.close()

    f = open(fileName3,'a')
    MFCC = librosa.feature.mfcc(y=y,sr=sr)
    x = np.mean(MFCC)
    y = np.std(MFCC)
    f.write(to_str(x))
    f.write(" ")
    f.write(to_str(y))
    f.write("\n")
    f.close()

#This method will read in the music
#and but it in the format to perform a comparison
def librosaCompare(readInWAVFile):
    y, sr = librosa.load(inputSong)
    S_full, phase = librosa.magphase(librosa.stft(y))

    S_filter = librosa.decompose.nn_filter(S_full,
                                       aggregate=np.median,
                                       metric='cosine',
                                       width=int(librosa.time_to_frames(2, sr=sr)))
    S_filter = np.minimum(S_full, S_filter)
    marginI, marginV = 2, 10
    power = 2
    mask_i = librosa.util.softmask(S_filter,
                               marginI * (S_full - S_filter),
                               power=power)

    mask_v = librosa.util.softmask(S_full - S_filter,
                               marginV * S_filter,
                               power=power)
    S_foreground = mask_v * S_full
    S_background = mask_i * S_full
    centralCentroid = librosa.feature.spectral_centroid(y=y,sr=sr)
    normalMean = np.mean(centralCentroid)
    normalSTD  = np.std(centralCentroid)
    vocalMean = np.mean(S_foreground)
    vocalSTD = np.std(S_foreground)

    extractVariable = []
    extractVariable.append(normalMean)
    extractVariable.append(normalSTD)
    extractVariable.append(vocalMean)
    extractVariable.append(vocalSTD)
    return extractVariable
