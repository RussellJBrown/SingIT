

from scipy.io.wavfile import read, write
import numpy
import sys
from aubio import source, pitch
import matplotlib.pyplot as plt
import os
import numpy as np
def to_str(var):
    return str(list(np.reshape(np.asarray(var), (1, np.size(var)))[0]))[1:-1]


locationEnglish = "/home/russell/SingIT/English"
locationGerman = "/home/russell/SingIT/German"
locationJapanese = "/home/russell/SingIT/Japanese"
locationFrench = "/home/russell/SingIT/French"

dirEnglish =  os.listdir(locationEnglish)
dirGerman =   os.listdir(locationGerman)
dirJapanese = os.listdir(locationJapanese)
dirFrench   = os.listdir(locationFrench)

Language = "French"
fileName3 = "Deessing"+Language+".txt"

for i in dirFrench:
    name, ext = os.path.splitext(i)
    print(ext)
    if(ext=='.wav'):
        name = os.path.splitext(i)[0]
        name2 = name[-3:]
        if (name2=="Out"):
            samplerate, data = read(locationFrench+"/"+i)
            numberOfDeessing = 0
            for i in data:
                if i > 0.02 and i < 0.1:
                    numberOfDeessing+=1

            f = open(fileName3,'a')
            f.write(to_str(numberOfDeessing))
            f.write("\n")
            f.close()
