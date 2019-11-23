# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
By Dabi Ahn. andabi412@gmail.com.
https://www.github.com/andabi
'''

# import matplotlib.pyplot as plt
import librosa
# import librosa.display
import numpy as np

filename = 'BonJovi.wav'
sr = 16000
n_fft = 4096
len_hop = n_fft / 4

########################################################################################################################
# Wav to STFT
########################################################################################################################

# Read 2-channel wav files
data, sr = librosa.load(filename, sr=sr, mono=False)

# Split wav into music and vocal parts
music_wav, vocal_wav = data
mix_wav = librosa.to_mono(data)

# Write each wav
librosa.output.write_wav('music.wav', music_wav, sr)
librosa.output.write_wav('vocal.wav', vocal_wav, sr)
librosa.output.write_wav('mix.wav', mix_wav, sr)

# Transform to spectrogram
D_music = librosa.stft(music_wav, n_fft=n_fft, hop_length=len_hop)
D_vocal = librosa.stft(vocal_wav, n_fft=n_fft, hop_length=len_hop)
D_mix = librosa.stft(mix_wav, n_fft=n_fft, hop_length=len_hop)

# magnitude and phase
magnitude_music, phase_music = np.abs(D_music), np.angle(D_music)
magnitude_vocal, phase_vocal = np.abs(D_vocal), np.angle(D_vocal)
magnitude_mix, phase_mix = np.abs(D_mix), np.angle(D_mix)


########################################################################################################################
# STFT to wav
########################################################################################################################

# Transform back to wav
music_wav_recon = librosa.istft(D_music, hop_length=len_hop)
vocal_wav_recon = librosa.istft(D_vocal, hop_length=len_hop)
mix_wav_recon = librosa.istft(D_mix, hop_length=len_hop)

# Write each reconstructed wav
librosa.output.write_wav('music_recon.wav', music_wav_recon, sr)
librosa.output.write_wav('vocal_recon.wav', vocal_wav_recon, sr)
librosa.output.write_wav('mix_recon.wav', mix_wav_recon, sr)
