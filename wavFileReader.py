from scipy.io import wavfile
import librosa
import librosa.display
import numpy as np

#read in list of wavefiles

def readInWav(wavList):
    for i in wavList:
        fs, data = wavfile.read(i)
        y, sr = librosa.load(i,duration=120)
        S_full, phase = librosa.magphase(librosa.stft(y))
        S_filter = librosa.decompose.nn_filter(S_full,
                                       aggregate=np.median,
                                       metric='cosine',
                                       width=int(librosa.time_to_frames(2, sr=sr)))


        S_filter = np.minimum(S_full, S_filter)
        margin_i, margin_v = 2, 10
        power = 2
        mask_v = librosa.util.softmask(S_full - S_filter,
                               margin_v * S_filter,
                               power=power)
        S_foreground = mask_v * S_full
        y_foreground = librosa.istft(S_foreground)
        output="99redBallons.wav"
        librosa.output.write_wav(output,y_foreground,fs)
        #plt.title('Foreground')
        #plt.colorbar()
        #plt.tight_layout()
        #plt.show()

if __name__ == "__main__" :
    readInWav(["/home/russell/LanguageIden/99 Red Balloons-Kvgz6swo-vY.wav"])
