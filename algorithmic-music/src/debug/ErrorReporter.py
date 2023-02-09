class ErrorReporter:

    instance = None

    def __init__(self, isEnabled):
        self.numerrs = 0
        self.errs = []
        self.isEnabled = isEnabled

    @staticmethod
    def getErrorReporter():
        if (instance == None):
            instance = ErrorReporter(True)
        return instance


    def addError(self, error):
        if not self.isEnabled:
            return
        self.errs = self.errs.append(error)

    def isErrors(self):
        return self.errs > 0

    def __str__(self) -> str:
        if (not self.isEnabled):
            return ''
        out = ''
        for err in self.errs:
            out += f'{err}\n'
        return out