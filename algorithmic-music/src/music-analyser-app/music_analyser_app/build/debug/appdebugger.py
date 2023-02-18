from debug.singleton import Singleton
from colorama import Fore, Back, Style
from debug.errorreporter import ErrorReporter

@Singleton
class AppDebugger:

    def __init__(self):
        self.errorReporter = ErrorReporter.instance()

    def log(self, message):
        print(Fore.WHITE, f'[DEBUG/Music Analyser] {message}')

    def error(self, error):
        self.errorReporter.addError(error)
        print(Fore.RED, f'[ERROR/Music Analyser] {error}', Fore.WHITE)
