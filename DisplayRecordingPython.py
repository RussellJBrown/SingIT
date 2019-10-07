import pyaudio
import numpy as np
from matplotlib import pyplot as plt

def displayRecording(displayAudio):
    p = pyaudio.PyAudio()
    if displayAudio is not None:
            plt.plot(displayAudio)
            plt.show()
    p.terminate()        
