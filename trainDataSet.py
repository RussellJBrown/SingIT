





#This method is the main method
#For training the dataset.
import sys
#from ReadLiveAudio import *
from CompareData import *
#from StoreData import *
from wavFileReader import *
from librosaVocalExtract import *
#DisplayData possible future feature
from timeit import default_timer as timer
import os
from pydub import AudioSegment
from vocalExtractFromCommandLine import *



if __name__ == '__main__':

    start = timer()
    locationEnglish = "/media/russell/775C-44EC/English"
    locationGerman = "/media/russell/775C-44EC/German"
    locationJapanese = "/media/russell/775C-44EC/Japanese"
    locationFrench = "/media/russell/775C-44EC/French"




    dirEnglish =  os.listdir(locationEnglish)
    dirGerman =   os.listdir(locationGerman)
    dirJapanese = os.listdir(locationJapanese)
    dirFrench = os.listdir(locationFrench)
    count = 0
    #for i in range(0,len(dirEnglish)):
     #  englishSong = dirEnglish[i]
      # name, ext = os.path.splitext(englishSong)
       #if(ext=='.wav'):
        #    count +=1
        #    print("Song Number: ")
        #    print(count)
        #    output = readInWav(locationEnglish+"/",englishSong,"English")
        #    betterVocalExtract(output)

    #for j in range(0,len(dirGerman)):
    #        print("Song Number: ")
    #        print(j)
    #        germanSong = dirGerman[j]
    #        if(ext=='.wav'):
    #            output = readInWav(locationGerman+"/",germanSong,"German")
    #            betterVocalExtract(output)

    #for k in range(0,len(dirJapanese)):
    #        print("Song Number:")
    #        print(k)
    #        japaneseSong = dirJapanese[k]
    #        name, ext = os.path.splitext(japaneseSong)
    #        if(ext=='.wav'):
    #            output = readInWav(locationJapanese+"/",japaneseSong,"Japanese")
    #            betterVocalExtract(output)

    #            '''
    for l in range(0,len(dirFrench)):
        print("Song Number: ")
        print(l)
        frenchSong = dirFrench[l]
        name, ext = os.path.splitext(frenchSong)
        if(ext=='.wav'):
            output = readInWav(locationFrench+"/",frenchSong,"French")
            betterVocalExtract(output)


    #trainDataset()
