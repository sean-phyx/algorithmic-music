import librosa as lr
import os
import soundfile as sf
import numpy as np
import subprocess
import matplotlib.pyplot as plt

def check_path(file_path):
    for root, dirs, files in os.walk(file_path):
        for file in files:
            print(file)
    
class ChromaGenerator:
    def __init__(self, chroma_type, sample_rate, frame_size, hop_size):
        self.chroma_type = chroma_type
        self.sample_rate = sample_rate
        self.frame_size = frame_size
        self.hop_size = hop_size
        self.chroma = None
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

        lr_audio, self.sample_rate = lr.load(file_path, sr=self.sample_rate)

        self.chroma = lr.feature.chroma_stft(y=lr_audio, sr=self.sample_rate)
        self.chroma_cq = lr.feature.chroma_cqt(y=lr_audio, sr=self.sample_rate)
        self.chroma_cens = lr.feature.chroma_cens(y=lr_audio, sr=self.sample_rate)
        self.chroma_stft = lr.feature.chroma_stft(y=lr_audio, sr=self.sample_rate)

    def mp3_to_wav(self, mp3_file_path):
        mp3_file_path_wav = mp3_file_path.replace(".mp3", ".wav")
        subprocess.call(['H:/algorithmic-music/algorithmic-music/algorithmic-music/ffmpeg-5.1.2-essentials_build/bin/ffmpeg.exe', '-i', mp3_file_path, mp3_file_path_wav, '-y'])

    def get_chroma(self):
        return self.chroma
    
    def get_chroma_cq(self):
        return self.chroma_cq
    
    def get_chroma_cens(self):
        return self.chroma_cens
    
    def get_chroma_stft(self):
        return self.chroma_stft
    
    def get_chroma_type(self):
        return self.chroma_type
    
    def get_sample_rate(self):
        return self.sample_rate
    
    def get_frame_size(self):
        return self.frame_size
    
    def get_hop_size(self):
        return self.hop_size

    def display_chroma(self, chroma_type):
        # TODO add logging
        try:
            if (chroma_type == "chroma"):
                lr.display.specshow(self.chroma, y_axis='chroma', x_axis='time')
            elif (chroma_type == "chroma_cq"):
                lr.display.specshow(self.chroma_cq, y_axis='chroma', x_axis='time')
            elif (chroma_type == "chroma_cens"):
                lr.display.specshow(self.chroma_cens, y_axis='chroma', x_axis='time')
            elif (chroma_type == "chroma_stft"):
                lr.display.specshow(self.chroma_stft, y_axis='chroma', x_axis='time')
            else:
                print("Invalid chroma type")
            plt.show()
        except Exception as e:
            # TODO: Add logging
            return
        
chroma = ChromaGenerator("chroma", 22050, 2048, 512)
chroma.generate_chroma('H:/algorithmic-music/algorithmic-music/algorithmic-music/example_files/beethovenfifth.mp3')
chroma.display_chroma("chroma")