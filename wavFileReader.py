from scipy.io import wavfile
from commandLineCall import *
import os
#read in list of wavefiles

def readInWav(wavFile):
        wavOut = os.path.splitext(wavFile)[0]
        wavOut = wavOut + "Out.wav"
        print(wavOut)
        commandExtractVocals(wavFile,wavOut)
        #fs, data = wavfile.read(wavOut)

        #plt.title('Foreground')
        #plt.colorbar()
        #plt.tight_layout()
        #plt.show()

if __name__ == "__main__" :
    readInWav("/home/russell/SingIT/99German.wav")
