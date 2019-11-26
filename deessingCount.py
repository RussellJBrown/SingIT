from aubio import source, pitch
from math import sqrt
import librosa
from sklearn.cluster import KMeans
import numpy as np
import sys
from librosaVocalExtract import *
from returnSubFiles import *


def des(song):
    from aubio import source,pitch
    win_s = 4096
    hop_s = 512
    samplerate = 44100
    s = source(song, samplerate, hop_s)
    samplerate = s.samplerate

    tolerance = 0.8

    pitch_o = pitch("yin", win_s, hop_s, samplerate)
    pitch_o.set_unit("midi")
    pitch_o.set_tolerance(tolerance)

    pitches = []
    confidences = []

    total_frames = 0
    countM = 0
    countF = 0
    while True:
        samples, read = s()
        pitch = pitch_o(samples)[0]
        pitches += [pitch]
        confidence = pitch_o.get_confidence()
        confidences += [confidence]
        total_frames += read
        if read < hop_s: break
        pList = list(pitches)
        mList = []
        fList = []
        for i in pList:
            tempI = i*100
            if tempI>=3000 and tempI<=6000:
                countM+=1
                mList.append(tempI)
            if tempI>=6000  and tempI<=8000:
                countF+=1
                fList.append(tempI)

    return countM,countF,mList,fList

if __name__ == '__main__':
    locationJapanese = "/home/russell/SingIT/outputJapanese"
    dirEnglish = getListOfFiles(locationJapanese)
    count = 0
    fileNames = "JapaneseDess.txt"
    fileNames2 = "femaleJapanese.txt"
    fileNames3 = "maleJapanese.txt"
    for i in dirEnglish:
        if "vocals.wav" in i:
            print(i)
            (countM,countF,mList,fList)=des(i)
            f = open(fileNames,'a')
            f.write(to_str(countM))
            f.write(" ")
            f.write(to_str(countF))
            f.write("\n")
            f.close()

            for j in mList:
                f=open(fileNames3,'a')
                f.write(to_str(j))
                f.write("\n")
                f.close()

            for k in fList:
                f=open(fileNames2,'a')
                f.write(to_str(k))
                f.write("\n")
                f.close()



            print("")
            print("Male: ")
            print(countM)
            print("")
            print("Female: ")
            print(countF)
            print("")
