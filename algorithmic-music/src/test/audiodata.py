#%%

import numpy as np
import matplotlib.pyplot as plt

import librosa;
import librosa.display;

# 1. Get the file path to an included audio example

filename = librosa.example('nutcracker')



# 2. Load the audio as a waveform `y`

#    Store the sampling rate as `sr`

y, sr = librosa.load(filename)

D = librosa.stft(y)  # STFT of y
S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

plt.figure()
librosa.display.specshow(S_db)
plt.colorbar()
#%%
