from math import sqrt
import librosa
from sklearn.cluster import KMeans
import numpy as np
import sys
from librosaVocalExtract import *
from returnSubFiles import *
def compareOutput(x,y):
    englishFile = "kClusteringEnglish.txt"
    frenchFile = "kClusteringFrench.txt"
    japaneseFile = "kClusteringJapanese.txt"
    germanFile = "kClusteringGerman.txt"
    english = "English"
    french = "French"
    german = "German"
    japanese = "Japanese"

    lowestDistance = [10000]*11
    lowestDistanceLanguage = ["Language Unkown"]*11

    channel_values = open(englishFile).read().split()
    Language = None
    for i in range(0,len(channel_values)):
         if i % 2 == 1:
             x2 = float(channel_values[i-1])
             y2 = float(channel_values[i])
             xt = x-x2
             yt = y-y2
             distance = sqrt(xt*xt+yt*yt)
             for i in range(0,len(lowestDistanceLanguage)):
                     lowestDistances = lowestDistance[i]
                     if distance<lowestDistances:
                        lowestDistance[i] = distance
                        lowestDistanceLanguage[i] = english
             lowestDistance, lowestDistanceLanguage = zip(*sorted(zip(lowestDistance, lowestDistanceLanguage),reverse=True))
             lowestDistance = list(lowestDistance)
             lowestDistanceLanguage = list(lowestDistanceLanguage)

    channel_values = open(frenchFile).read().split()
    for i in range(0,len(channel_values)):
        if i%2==1:
             x2 = float(channel_values[i-1])
             y2 = float(channel_values[i])
             xt = x-x2
             yt = y-y2
             distance = sqrt(xt*xt+yt*yt)
             for i in range(0,len(lowestDistanceLanguage)):
                 lowestDistances = lowestDistance[i]
                 if distance<lowestDistances:
                     lowestDistance[i] = distance
                     lowestDistanceLanguage[i] = french
             lowestDistance, lowestDistanceLanguage = zip(*sorted(zip(lowestDistance, lowestDistanceLanguage),reverse=True))
             lowestDistance = list(lowestDistance)
             lowestDistanceLanguage = list(lowestDistanceLanguage)

    channel_values=open(germanFile).read().split()
    for i in range(0,len(channel_values)):
         if i % 2 == 1:
             x2 = float(channel_values[i-1])
             y2 = float(channel_values[i])
             xt = x-x2
             yt = y-y2
             distance = sqrt(xt*xt+yt*yt)
             for i in range(0,len(lowestDistanceLanguage)):
                lowestDistances = lowestDistance[i]
                if distance<lowestDistances:
                     lowestDistance[i] = distance
                     lowestDistanceLanguage[i] = german
             lowestDistance, lowestDistanceLanguage = zip(*sorted(zip(lowestDistance, lowestDistanceLanguage),reverse=True))
             lowestDistance = list(lowestDistance)
             lowestDistanceLanguage = list(lowestDistanceLanguage)

    channel_values=open(japaneseFile).read().split()
    for i in range(0,len(channel_values)):
         if i % 2 == 1:
             x2 = float(channel_values[i-1])
             y2 = float(channel_values[i])
             xt = x-x2
             yt = y-y2
             distance = sqrt(xt*xt+yt*yt)
             for i in range(0,len(lowestDistanceLanguage)):
                 lowestDistances = lowestDistance[i]
                 if distance<lowestDistances:
                     lowestDistance[i] = distance
                     lowestDistanceLanguage[i] = japanese
             lowestDistance, lowestDistanceLanguage = zip(*sorted(zip(lowestDistance, lowestDistanceLanguage),reverse=True))
             lowestDistance = list(lowestDistance)
             lowestDistanceLanguage = list(lowestDistanceLanguage)







    eCount = 0
    fCount = 0
    jCount = 0
    gCount = 0
    for i in range(0,len(lowestDistanceLanguage)):
        language = lowestDistanceLanguage[i]
        if (language==english):
            eCount += 1
        if (language==french):
            fCount += 1
        if (language==german):
            gCount += 1
        if (language==japanese):
            jCount += 1

    if eCount > fCount and eCount>jCount and eCount>gCount:
        Language = english

    elif fCount> eCount and fCount>jCount and fCount>gCount:
        Language = french
    elif gCount> eCount and gCount>fCount and gCount>jCount:
        Language = german
    elif jCount>eCount and jCount>fCount and jCount>gCount:
        Language = japanese
    else:
        Language = "Unknown"


    print("Language Returned: " + Language)
    return Language




def spectral_centroid(x, samplerate=44100):
    magnitudes = np.abs(np.fft.rfft(x)) # magnitudes of positive frequencies
    length = len(x)
    freqs = np.abs(np.fft.fftfreq(length, 1.0/samplerate)[:length//2+1]) # positive frequencies
    return np.sum(magnitudes*freqs) / np.sum(magnitudes) # return weighted mean




def kMeanLiveAudio(song):
    listLangauge = []
    X,sr = librosa.load(song)
    centroid= spectral_centroid(X)
    Kmean = KMeans(n_clusters=21)
    X = np.reshape(X, (-1, 2))
    Kmean.fit(X)
    kCluster = Kmean.cluster_centers_
    rows = kCluster.shape[0]
    cols = kCluster.shape[1]
    #0: x>3000
    #1: 3000>x and 3300<x
    #2: 3300<x and 3600>x
    #3: 3600<x and 3900>x
    #4: 3900<x and 4200>x
    #5: 4200<x and 4500>x
    #6: 4500<x and 4800>x
    #7: 4800<x and 5200>x
    #8: 5200<x and 5500>x
    #9: 5500<x and 5800>x
    #10:5800<x and 6000>x
    #11:6000<x
    histogram = [0]*25
    for i in range(0,rows):
        for j in range(0,cols):
            if j%2==0:
                x = kCluster[i,j]*10000
                y = kCluster[i,j+1]*10000
                num = sqrt(x*x+y*y)
                num=centroid-num
                if 500>num:
                    histogram[0]+=1
                elif num>=500 and 800>num:
                    histogram[1]+=1
                elif num>=800 and 1100>num:
                    histogram[2]+=1
                elif num>=1100 and 1400>num:
                    histogram[3]+=1
                elif num>=1400 and 1700>num:
                    histogram[4]+=1
                elif num>=1700 and 2100>num:
                    histogram[5]+=1
                elif num>=2100 and 2400>num:
                    histogram[6]+=1
                elif num>=2400 and 2700>num:
                    histogram[7]+=1
                elif num>=2700 and 3000>num:
                    histogram[8]+=1
                elif num>=3000 and 3300>num:
                    histogram[9]+=1
                elif num>=3300 and 3600>num:
                    histogram[10]+=1
                elif num>=3600 and 3900>num:
                    histogram[11]+=1
                elif num>=3900 and 4200>num:
                    histogram[12]+=1
                elif num>=4200 and 4500>num:
                    histogram[13]+=1
                elif num>=4500 and 4800>num:
                    histogram[14]+=1
                elif num>=4800 and 5200>num:
                    histogram[15]+=1
                elif num>=5200 and 5500>num:
                    histogram[16]+=1
                elif num>=5500 and 5800>num:
                    histogram[17]+=1
                elif num>=5800 and 6100>num:
                    histogram[18]+=1
                elif num>=6100 and 6400>num:
                    histogram[19]+=1
                elif num>=6400 and 6700>num:
                    histogram[20]+=1
                elif num>=6700 and 7000>num:
                    histogram[21]+=1
                elif num>=7000 and 7300>num:
                    histogram[22]+=1
                elif num>=7600 and 7900>num:
                    histogram[23]+=1
                elif num>=7900:
                    histogram[24]+=1
    return histogram



def testDataSet():
    locationJapanese = "/home/russell/SingIT/outputFrench"
    dirEnglish = getListOfFiles(locationJapanese)
    histogramFinal = [0]*25
    count = 0
    fileNames = "FrenchHist.txt"
    for i in dirEnglish:
        print(i)
        if "vocals.wav" in i:
                count+=1
                print("Count: ")
                print(count)
                Language="temp"
                histogram=kMeanLiveAudio(i)
                print(histogram)
                for i in range(0,len(histogramFinal)):
                    histogramFinal[i]= histogramFinal[i] +  histogram[i]


    for i in range(0,len(histogramFinal)):
        histogramFinal[i]= (histogramFinal[i]/(21*count))
    f = open(fileNames,'a')
    f.write(to_str(histogramFinal))
    f.write("\n")
    f.close()
    print(histogramFinal)


if __name__ == '__main__':
    #Currently Being Used for Testing
    testDataSet()
    #kMeanLiveAudio(song)
    #print(count)
