from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import librosa

import librosa.display

#This program attempts to get
#librosa to work, may need to remove later
y, sr = librosa.load('99German.wav')
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

print(beat_frames)
print(tempo)
print(beat_times)
