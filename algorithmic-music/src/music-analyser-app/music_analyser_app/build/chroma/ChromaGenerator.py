#%%
import librosa as lr
from librosa.display import specshow
import os
import soundfile as sf
import numpy as np
import subprocess
import matplotlib.pyplot as plt
    
class ChromaGenerator:
    def __init__(self, sample_rate, frame_size, hop_size):
        self.sample_rate = sample_rate
        self.frame_size = frame_size
        self.duration = frame_size / sample_rate
        self.hop_size = hop_size
        self.chroma_cq = None
        self.chroma_cens = None
        self.chroma_stft = None

    def generate_chroma(self, file_path):

        if file_path.endswith(".mp3"):
            if (os.path.isfile(file_path.replace(".mp3", ".wav"))):
                file_path = file_path.replace(".mp3", ".wav")
            else:
                self.mp3_to_wav(file_path)
                file_path = file_path.replace(".mp3", ".wav")

        lr_audio, self.sample_rate = lr.load(file_path, sr=self.sample_rate, duration=self.duration)

        self.chroma_cq = lr.feature.chroma_cqt(y=lr_audio, sr=self.sample_rate)
        self.chroma_cens = lr.feature.chroma_cens(y=lr_audio, sr=self.sample_rate)
        self.chroma_stft = lr.feature.chroma_stft(y=lr_audio, sr=self.sample_rate)

    def mp3_to_wav(self, mp3_file_path):
        mp3_file_path_wav = mp3_file_path.replace(".mp3", ".wav")
        subprocess.call(['C:/Users/armat/Documents/algorithmic-music/algorithmic-music/required/ffmpeg-5.1.2-essentials_build/bin/ffmpeg.exe', '-i', mp3_file_path, mp3_file_path_wav, '-y'])
    
    def set_duration(self, duration):
        self.duration = duration

    def display_chroma(self, chroma):
        fig, ax = plt.subplots()
        fig.set_size_inches(24, 12)
        img = specshow(chroma, ax=ax)
        fig.colorbar(img, ax=ax)

    def save_chroma(self, chroma, file_path):
        plt.figure(figsize=(24,8))
        timestamps = lr.frames_to_time(range(len(chroma[0])), sr=self.sample_rate)
        specshow(chroma, y_axis='chroma', x_axis='time')
        plt.colorbar()
        xticks = np.arange(0, timestamps[-1], 1)
        plt.xticks(xticks, rotation=90)
        plt.yticks(range(12), ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'])
        plt.tight_layout()
        plt.savefig(file_path, bbox_inches='tight', pad_inches=0, dpi=300)
        
chroma = ChromaGenerator(22050, 2048, 512)
chroma.set_duration(5)
print(os.path.isfile('C:/Users/armat/Documents/algorithmic-music/algorithmic-music/example_files/beethovenfifth.mp3'))
chroma.generate_chroma('C:/Users/armat/Documents/algorithmic-music/algorithmic-music/example_files/beethovenfifth.mp3')
# chroma.display_chroma(chroma.chroma_cq)
chroma.save_chroma(chroma.chroma_cq, 'C:/Users/armat/Documents/algorithmic-music/algorithmic-music/example_files/beethovenfifth.png')
# %%
