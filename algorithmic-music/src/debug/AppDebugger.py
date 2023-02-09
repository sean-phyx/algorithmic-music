from colorama import Fore, Back, Style
import ErrorReporter

class AppDebugger:

    instance = None

    def __init__(self, isEnabled):
        self.isEnabled = isEnabled
        self.instance = None
    
    @staticmethod
    def getDebugger():
        if (instance == None):
            instance = AppDebugger(True)
        return instance

    def log(self, message):
        print(Fore.WHITE, f'[DEBUG/Music Analyser] {message}')

    def error(self, error):
        print(Fore.RED, f'[ERROR/Music Analyser] {error}')
