
import pyaudio
import wave
from librosaVocalExtract import *
from compareOut import *

#The reading in Live audio was taken from
#StackOverFlow from User: Yevhen Kuzmovych and alr
#From: https://stackoverflow.com/questions/35344649/reading-input-sound-signal-using-python
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
    readInLiveAudio()
    libroExtract("output.wav","testLanguage")
    Language = kMeanLiveAudio("output.wav")
    print("The Language is: " +  Language)
