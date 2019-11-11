from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

def to_str(var):
    return str(list(np.reshape(np.asarray(var), (1, np.size(var)))[0]))[1:-1]


def libroExtract(inputSong):
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

    #TODO: change to a string variable and add if statements for
    #other languages
    f = open('NormalScatterEnglish.txt','a')
    f.write(to_str(normalMean))
    f.write(" ")
    f.write(to_str(normalSTD))
    f.write("\n")
    f.close()

    #Currently Checking here for errors

    vocalMean = np.mean(S_foreground)
    vocalSTD = np.std(S_foreground)
    f = open('VocalExtractedScatterEnglish.txt','a')
    f.write(to_str(vocalMean))
    f.write(" ")
    f.write(to_str(vocalSTD))
    f.write("\n")
    f.close()
