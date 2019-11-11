from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import librosa

import librosa.display
import numpy as np

y, sr = librosa.load('Nena ‎- 99 Luftballons-La4Dcd1aUcE.wav')
# And compute the spectrogram magnitude and phase
S_full, phase = librosa.magphase(librosa.stft(y))
S_filter = librosa.decompose.nn_filter(S_full,
                                       aggregate=np.median,
                                       metric='cosine',
                                       width=int(librosa.time_to_frames(2, sr=sr)))
S_filter = np.minimum(S_full, S_filter)
margin_i, margin_v = 2, 10
power = 2

mask_i = librosa.util.softmask(S_filter,
                               margin_i * (S_full - S_filter),
                               power=power)

mask_v = librosa.util.softmask(S_full - S_filter,
                               margin_v * S_filter,
                               power=power)

# Once we have the masks, simply multiply them with the input spectrum
# to separate the components
S_foreground = mask_v * S_full
S_background = mask_i * S_full
mean = np.mean(S_foreground)
std = np.std(S_foreground)

print(mean)
print(std)
