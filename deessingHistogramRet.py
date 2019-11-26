import librosa
import os
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def returnHist():
    englishf = []
    englishm = []

    germanf = []
    germanm = []

    japanesef = []
    japanesem = []

    frenchf = []
    frenchm = []
    with open('/home/russell/SingIT/maleEnglish.txt', 'r') as file:
        data = file.read()
        data = data.split("\n")
        count=0
        for i in data:
                try:
                    englishm.append(float(i)+1)
                except:
                    pass
    with open('/home/russell/SingIT/femaleEnglish.txt', 'r') as file:
        data = file.read()
        data = data.split("\n")
        count=0
        for i in data:
                try:
                    englishf.append(float(i))
                except:
                    pass

    with open('/home/russell/SingIT/maleFrench.txt', 'r') as file:
        data = file.read()
        data = data.split("\n")
        count=0
        for i in data:
                try:
                    frenchm.append(float(i))
                except:
                    pass
    with open('/home/russell/SingIT/femaleFrench.txt', 'r') as file:
        data = file.read()
        data = data.split("\n")
        count=0
        for i in data:
                try:
                    frenchf.append(float(i))
                except:
                    pass


    with open('/home/russell/SingIT/maleGerman.txt', 'r') as file:
        data = file.read()
        data = data.split("\n")
        count=0
        for i in data:
                try:
                    germanm.append(float(i))
                except:
                    pass
    with open('/home/russell/SingIT/femaleGerman.txt', 'r') as file:
        data = file.read()
        data = data.split("\n")
        count=0
        for i in data:
                try:
                    germanf.append(float(i))
                except:
                    pass



    with open('/home/russell/SingIT/maleJapanese.txt', 'r') as file:
        data = file.read()
        data = data.split("\n")
        count=0
        for i in data:
                try:
                    japanesem.append(float(i))
                except:
                    pass
    with open('/home/russell/SingIT/femaleJapanese.txt', 'r') as file:
        data = file.read()
        data = data.split("\n")
        count=0
        for i in data:
                try:
                    japanesef.append(float(i))
                except:
                    pass


    dataEM = np.asarray(englishm, dtype=np.float32)
    dataEF = np.asarray(englishm, dtype=np.float32)

    dataFM = np.asarray(frenchm, dtype=np.float32)
    dataFF = np.asarray(frenchf, dtype=np.float32)

    dataGM = np.asarray(germanm, dtype=np.float32)
    dataGF = np.asarray(germanf, dtype=np.float32)

    dataJM = np.asarray(japanesem, dtype=np.float32)
    dataJF = np.asarray(japanesef, dtype=np.float32)

    observedEM, _ = np.histogram(dataEM, bins=100, range=[3000, 6000])
    observedEF, _ = np.histogram(dataEF, bins=100, range=[6000, 8000])

    observedFM, _ = np.histogram(dataFM, bins=100, range=[3000, 6000])
    observedFF, _ = np.histogram(dataFF, bins=100, range=[6000, 8000])

    observedGM, _ = np.histogram(dataGM, bins=100, range=[3000, 6000])
    observedGF, _ = np.histogram(dataGF, bins=100, range=[6000, 8000])

    observedJM, _ = np.histogram(dataJM, bins=100, range=[3000, 6000])
    observedJF, _ = np.histogram(dataJF, bins=100, range=[6000, 8000])


    observedEM = observedEM + 1
    observedEF = observedEF + 1

    observedFM = observedFM + 1
    observedFF = observedFF + 1

    observedGM = observedGM + 1
    observedGF = observedGF + 1

    observedJM = observedJM + 1
    observedFJ = observedJF + 1


    return observedEM, observedEF, observedFM, observedFF, observedGM, observedGF, observedJM, observedJF
