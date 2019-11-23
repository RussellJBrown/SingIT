import pyaudio
import numpy as np
from matplotlib import pyplot as plt




def liveAudio():
    CHUNK = 4096 # number of data points to read at a time
    RATE = 44100 # time resolution of the recording device (Hz)

    p=pyaudio.PyAudio() # start the PyAudio class
    stream=p.open(format=pyaudio.paInt16,channels=2,rate=RATE,input=True,
                  frames_per_buffer=CHUNK) #uses default input device

    # create a numpy array holding a single read of audio data
    for i in range(100): #to it a few times just to see
        data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
        print(data)

    # close the stream gracefully
    stream.stop_stream()
    stream.close()
    p.terminate()
