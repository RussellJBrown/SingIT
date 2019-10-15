
#This method calls the command line
#ffmpeg in order to try and remove the highpass and lowpass filters
import os
def commandExtractVocals(inputFile, outputFile):
    line = 'ffmpeg -i ' + inputFile + ' -af "highpass=f=100, lowpass=f=9000" + ' + outputFile
    os.system(line)  
