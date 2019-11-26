import os
import sys
#Runs Spleeter command on Song
def betterVocalExtract(song):
    song = '"'+song+'"'
    command = "spleeter separate -i "+ song + " -p spleeter:2stems -o outputFrench"
    print("Start Command")
    os.system(command)
    print("Finished Command")




def betterVocalExtractTest(song,outputLocation):
    song = '"'+song+'"'
    command = "spleeter separate -i "+ song + " -p spleeter:2stems -o " + outputLocation
    print("Start Command" + command)
    os.system(command)
    print("Finished Command")
