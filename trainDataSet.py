





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

def convertMP3(path,str):

    for i in str:
        iNew= path+i
        print(iNew)
        name = os.path.splitext(iNew)[0]
        extension = os.path.splitext(iNew)[1]
        if(extension==".mp3"):
            sound = AudioSegment.from_mp3(iNew)
            name = name+".wav"
            sound.export(name,format="wav")
            os.remove(iNew)



if __name__ == '__main__':

    start = timer()
    locationEnglish = "/home/russell/SingIT/English"
    locationGerman = "/home/russell/SingIT/German"
    locationJapanese = "/home/russell/SingIT/Japanese"
    locationFrench = "/home/russell/SingIT/French"



    dirEnglish =  os.listdir(locationEnglish)
    #convertMP3(locationEnglish+"/",dirEnglish)
    dirGerman =   os.listdir(locationGerman)
    #convertMP3(locationGerman+"/",dirGerman)
    dirJapanese = os.listdir(locationJapanese)
    #convertMP3(locationJapanese+"/",dirJapanese)
    dirFrench   = os.listdir(locationFrench)
    #convertMP3(locationFrench+"/",dirFrench)

    dirEnglish =  os.listdir(locationEnglish)
    dirGerman =   os.listdir(locationGerman)
    dirJapanese = os.listdir(locationJapanese)
    dirFrench = os.listdir(locationFrench)

    #for i in range(0,len(dirEnglish)):
     #  print("Song Number: ")
      # print(i)
       #englishSong = dirEnglish[i]
       #name, ext = os.path.splitext(englishSong)
       #if(ext=='.wav'):
        #    output = readInWav(locationEnglish+"/",englishSong,"English")


    #for j in range(0,len(dirGerman)):
    #        print("Song Number: ")
    #        print(j)
    #        germanSong = dirGerman[j]
    #        name, ext = os.path.splitext(germanSong)
    #        if(ext=='.wav'):
    #             output = readInWav(locationGerman+"/",germanSong,"German")

    for k in range(0,len(dirJapanese)):
            print("Song Number:")
            print(k)
            japaneseSong = dirJapanese[k]
            name, ext = os.path.splitext(japaneseSong)
            if(ext=='.wav'):
                output = readInWav(locationJapanese+"/",japaneseSong,"Japanese")
    #            '''
    #for l in range(0,len(dirFrench)):
    #    print("Song Number: ")
    #    print(l)
    #    frenchSong = dirFrench[l]
    #    name, ext = os.path.splitext(frenchSong)
    #    if(ext=='.wav'):
    #        output = readInWav(locationFrench+"/",frenchSong,"French")
    #        '''

    #trainDataset()
