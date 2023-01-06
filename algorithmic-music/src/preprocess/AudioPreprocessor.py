import soundfile as sf
import numpy as np
import colorama
import scipy.signal

class AudioPreprocessor:

    def __init__(self, audiofile):
        self.audiofile = audiofile
        self.audioasNpArray = None

    def convertToNumpy(self):
        """Converts the audio to a numpy array

        Parameters:
        None

        Returns:
        numpy array representing the audio file

        """
        self.audioasNpArray = sf.read(self.audiofile)
        return self.audioasNpArray

    def convertToNumpy(self):
        self.audioasNpArray = sf.read(self.audiofile)

    def generateSTFT(self):
        # check if the audio is already an np array, if not, turn it into one and alert this
        if (self.audioasNpArray == None):
            self.convertToNumpy()
            print(f'{colorama.Fore.YELLOW}[WARN] Converted audiofile to np array as it was None {colorama.Fore.WHITE}')
        
        # generate the STFT with scipy
        self.STFT = scipy.signal.stft(self.audioasNpArray, fs=44100, window='hann', nperseg=1024, noverlap=512)

        return self.STFT