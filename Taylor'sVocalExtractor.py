#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Copied from the Librosa GitHub and modified to play the ISTFT of the foreground as an audio file.

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import librosa

import librosa.display

import IPython.display as ipd

y, sr = librosa.load("reggae.00000.wav")
#y = y[:len(y)//5]
S_full, phase = librosa.magphase(librosa.stft(y))

S_filter = librosa.decompose.nn_filter(S_full,aggregate=np.median,metric='cosine',width=int(librosa.time_to_frames(2, sr=sr)))
S_filter = np.minimum(S_full, S_filter)
margin_v = 10    # The lower this number, the higher the vocal quality, but lower the amount of instrument reduction.
power = 2
mask_v = librosa.util.softmask(S_full - S_filter,margin_v * S_filter,power=power)
S_foreground = mask_v * S_full

# Uncomment the following for the background.
# margin_i = 2
# mask_i = librosa.util.softmask(S_filter,margin_i * (S_full - S_filter),power=power)
# S_background = mask_i * S_full

ipd.Audio(librosa.istft(S_foreground), rate=sr) # load a local WAV file

