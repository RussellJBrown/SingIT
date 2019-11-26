
import pyaudio
import wave
from librosaVocalExtract import *
from compareOut import *
from readHistograms import *
from vocalExtractFromCommandLine import *
from deessingHistogramRet import *
from deessingCount import *
#The reading in Live audio was taken from
#StackOverFlow from User: Yevhen Kuzmovych and alr
#From: https://stackoverflow.com/questions/35344649/reading-input-sound-signal-using-python
def ComputeChiSquareGOF(expected, observed):
    expected_scaled = expected / float(sum(expected)) * sum(observed)
    result = stats.chisquare(f_obs=observed, f_exp=expected_scaled)
    return result[1]

def readInLiveAudio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = "output.wav"
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print("* recording")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("* done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


if __name__ == '__main__':
    #readInLiveAudio()
    (observedEM, observedEF, observedFM, observedFF, observedGM, observedGF, observedJM, observedJF) = returnHist()
    location = "/home/russell/SingIT/testFrench"
    mainLocation = "/home/russell/SingIT"
    newLocation = "testEnglishVE"
    dirEnglish =  os.listdir(location)
    for i in range(0,len(dirEnglish)):
        EnglishSong = dirEnglish[i]
        fileNameM = EnglishSong  + "male222" + ".txt"
        fileNameF = EnglishSong  + "female222"+".txt"
        name, ext = os.path.splitext(EnglishSong)
        if ext == ".wav":
            output=libroExtract(location+"/"+dirEnglish[i],"test")
            betterVocalExtractTest(output,newLocation)

    locationOfCleanOutput = mainLocation+"/"+newLocation
    dirEnglish = getListOfFiles(locationOfCleanOutput)
    for i in dirEnglish:
                if "vocals.wav" in i:
                    (countM,countF,mList,fList)=des(i)

                    countEM = np.asarray(mList, dtype=np.float32)
                    countEF = np.asarray(fList, dtype=np.float32)



                    observedEM=observedEM[:-1]
                    observedFM =observedFM[:-1]
                    observedGM = observedGM[:-1]
                    observedJM= observedJM[:-1]

                    observedEF = observedEF[:-1]
                    observedFF = observedFF[:-1]
                    observedGF = observedGF[:-1]
                    observedF = observedJF[:-1]


                    enM, _ = np.histogram(countEM, bins=100, range=[3000, 6000])
                    enF, _ = np.histogram(countEF, bins=100, range=[6000, 9000])

                    enOM, _ =  np.histogram(observedEM, bins=100, range=[3000, 6000])
                    enOF, _ =  np.histogram(observedEF, bins=100, range=[6000, 9000])

                    frOM, _ =  np.histogram(observedFM, bins=100, range=[3000, 6000])
                    frOF, _ =  np.histogram(observedFF, bins=100, range=[6000, 9000])

                    grOM, _ =  np.histogram(observedGM, bins=100, range=[3000, 6000])
                    grOF, _ =  np.histogram(observedGF, bins=100, range=[6000, 9000])

                    jpOM, _ =  np.histogram(observedJM, bins=100, range=[3000, 6000])
                    jpOF, _ =  np.histogram(observedJF, bins=100, range=[6000, 9000])

                    #expected = expected + 1
                    #observed = observed + 1
                    enM = enM +1
                    enF = enF+1
                    enOM = enOM+1
                    enOF = enOF+1

                    frOM = frOM+1
                    frOF = frOF+1

                    grOM = grOM+1
                    grOF = grOF+1

                    jpOM = jpOM+1
                    jpOF = jpOF+1

                    pValueM = ComputeChiSquareGOF(enM, enOM)
                    pValue2M = ComputeChiSquareGOF(enM, frOM)
                    pValue3M =  ComputeChiSquareGOF(enM, grOM)
                    pValue4M =  ComputeChiSquareGOF(enM, jpOM)

                    pValueF = ComputeChiSquareGOF(enF, enOF)
                    pValue2F = ComputeChiSquareGOF(enF, frOF)
                    pValue3F =  ComputeChiSquareGOF(enF, grOF)
                    pValue4F =  ComputeChiSquareGOF(enF, jpOF)

                    print(pValueM)
                    print(pValue2M)
                    print(pValue3M)
                    print(pValue4M)


                    print(pValueF)
                    print(pValue2F)
                    print(pValue3F)
                    print(pValue4F)



                    value = []
                    lang = []
                    value.append(pValueM)
                    lang.append("English")
                    value.append(pValue2M)
                    lang.append("French")
                    value.append(pValue3M)
                    lang.append("German")
                    value.append(pValue4M)
                    lang.append("Japanese")

                    value.append(pValueF)
                    lang.append("English")
                    value.append(pValue2F)
                    lang.append("French")
                    value.append(pValue3F)
                    lang.append("German")
                    value.append(pValue4F)
                    lang.append("Japanese")

                    index=value.index(max(value))
                    print("Language is:  " + lang[index])
