





#This method is the main method
#The Language Identification System
#will have multiple options when running
#Option 1: Train a Dataset
#Option 2: Play a Song to determine the language of the Song
#Insert more Options here...
import sys
#from ReadLiveAudio import *
from CompareData import *
from StoreData import *
from wavFileReader import *
#DisplayData possible future feature
if __name__ == '__main__':
    locationEnglish = ""
    locationGerman = ""
    locationJapanese = ""
    locationFrench

    dirEnglish =  os.listdir(listLocation)
    dirGerman =   os.listdir(listLocation)
    dirJapanese = os.listdir(listLocation)
    dirFrench   = os.listdir(listLocation)
    for i in range(0,len(dirEnglish)):
        englishSong = dirEnglish[i]
        output = wavFileReader(englishSong)

    for j in range(0,len(dirGerman)):
        germanSong = dirGerman[j]
        output = waveFileReader(germanSong)

    for k in range(0,len(dirJapanese)):
        japaneseSong = dirJapanese[k]
        output = waveFileReader(japaneseSong)

    for l in range(0,len(dirFrench)):
        frenchSong = dirFrench[l]
        output = waveFileReader(fenchSong)


    trainDataset()
