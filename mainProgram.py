





#This method is the main method
#The Language Identification System
#will have multiple options when running
#Option 1: Train a Dataset
#Option 2: Play a Song to determine the language of the Song
#Insert more Options here...
import sys
from ReadLiveAudio import *
from CompareData import *
from StoreData import *
#DisplayData possible future feature
if __name__ == '__main__':
    print("TD for Train Dataset or DSL for Determine Song Language ")
    text = input("Train Dataset or Determine Song Language?")
    if text == "TD":
        #run TD
        print("temp")


    elif text == "DSL":
        #run ReadLiveAUdio
        #run Data Comparsion
        print("temp")
