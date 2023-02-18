from debug.singleton import Singleton

@Singleton
class ErrorReporter:

    def __init__(self):
        self.numerrs = 0
        self.errs = []

    def addError(self, error):
        self.errs.append(error)

    def isErrors(self):
        return self.errs > 0

    def __str__(self) -> str:
        out = ''
        for err in self.errs:
            out += f'{err}\n'
        return out