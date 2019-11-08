#Certain Consantants are harder
#to identify as such removing them
#needs to be done this is
#done by applying a band filters



from scipy.signal import butter, lfilter,freqz
import numpy as np

fs,signal = wav.read("99English.wav")
t = np.arrange(fs)/fs
sinWav = np.sin(2*np.pi*signal*t)

fc = 2000 #current
w = fc / (fs/2)
b,a = signal.butter(5,w,'low')
output = signal.filtfilt(b, a, signal)
write("99English.wav",fs,output)
