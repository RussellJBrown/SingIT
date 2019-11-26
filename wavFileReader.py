from scipy.io import wavfile
from commandLineCall import *
from librosaVocalExtract import *
import os
#read in list of wavefiles

def readInWav(local, wavFile,Language):
        wavFile = local+wavFile
        outFile=libroExtract(wavFile,Language)
        return outFile
        #nextPhase(outFile,Language)
        #commandExtractVocals(wavFile,wavOut)
        #fs, data = wavfile.read(wavOut)
        #plt.title('Foreground')
        #plt.colorbar()
        #plt.tight_layout()
        #plt.show()
