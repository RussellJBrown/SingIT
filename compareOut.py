from math import sqrt
import librosa
from sklearn.cluster import KMeans
import numpy as np
from librosaVocalExtract import *
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



def kMeanLiveAudio(song):
    listLangauge = []
    X,sr = librosa.load(song)
    Kmean = KMeans(n_clusters=21)
    X = np.reshape(X, (-1, 2))
    Kmean.fit(X)
    kCluster=Kmean.cluster_centers_
    rows = kCluster.shape[0]
    cols = kCluster.shape[1]
    for i in range(0,rows):
        for j in range(0,cols):
            if j%2==0:
                x = kCluster[i,j]
                y = kCluster[i,j+1]
                language = compareOutput(x,y)
                listLangauge.append(language)

    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    for i in listLangauge:
        if i == "English":
            count1+=1
        elif i== "French":
            count2+=1
        elif i == "German":
            count3+=1
        elif i == "Japanese":
            count4+=1
        else:
            count5+=1
    if  count1>count2 and count1>count3 and count1>count4:
        Language = "English"

    elif count2>count1 and count2>count3 and count2>count4:
        Language = "French"

    elif count3>count1 and count3>count2 and count3>count4:
        Language = "German"

    elif count4>count1 and count3>count2 and count4>count3:
        Language = "Japanese"
    else:
        Language = "Unknown Lanuage"


    return Language



def testDataSet():
    locationJapanese = "/home/russell/SingIT/French"
    dirEnglish =  os.listdir(locationJapanese)
    count = 0
    for i in dirEnglish:
        name, ext = os.path.splitext(i)
        out=name[-3:]
        if(ext=='.wav' and out == "Out"):
            song = locationJapanese+"/"+i
            print(song)
            Language=kMeanLiveAudio(song)
            if Language == "French":
                count += 1
            print("The Language and Count is: " + Language)
            print("")
            print("")
    print(count)



if __name__ == '__main__':
    #Currently Being Used for Testing
    kMeanLiveAudio(song)
    print(count)
