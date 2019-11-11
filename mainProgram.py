





#This method is the main method
#The Language Identification System
#will have multiple options when running
#Option 1: Train a Dataset
#Option 2: Play a Song to determine the language of the Song
#Insert more Options here...
import sys
#from ReadLiveAudio import *
from CompareData import *
#from StoreData import *
from wavFileReader import *
from librosaVocalExtract import *
#DisplayData possible future feature
from timeit import default_timer as timer
if __name__ == '__main__':

    start = timer()
    locationEnglish = "/home/russell/SingIT/English"
    locationGerman = "/home/russell/SingIT/German"
    locationJapanese = "/home/russell/SingIT/Japanese"
    locationFrench = "/home/russell/SingIT/French"

    dirEnglish =  os.listdir(locationEnglish)
    dirGerman =   os.listdir(locationGerman)
    dirJapanese = os.listdir(locationJapanese)
    dirFrench   = os.listdir(locationFrench)
    #for i in range(0,len(dirEnglish)):
    #    print("Song Number: ")
    #    print(i)
    #    englishSong = dirEnglish[i]
    #    name, ext = os.path.splitext(englishSong)
    #    if(ext=='.wav'):
    #        output = readInWav(locationEnglish+"/",englishSong)

    #end = timer()
    #print(end-start)

    #for j in range(0,len(dirGerman)):
#    germanSong = dirGerman[j]
#        output = waveFileReader(germanSong)

    #for k in range(0,len(dirJapanese)):
#    print("Song Number:")
#        print(k)
#        japaneseSong = dirJapanese[k]
##        if(ext=='.wav'):
#                output = readInWav(locationJapanese+"/",japaneseSong)

    for l in range(0,len(dirFrench)):
        print("Song Number: ")
        print(l)
        frenchSong = dirFrench[l]
        name, ext = os.path.splitext(frenchSong)
        if(ext=='.wav'):
            output = readInWav(locationFrench+"/",frenchSong)


    #trainDataset()
