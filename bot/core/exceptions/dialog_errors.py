class BaseInputError(ValueError):
    def __init__(self, message):
        super().__init__(message)

class NameInputError(BaseInputError):
    def __init__(self):
        msg = ('Invalid name. '
               'The name must be a string of at least 2 characters '
               'and include no more than 1 word or the words must be separated by ‘-’.')
        super().__init__(msg)

class ScoreNameInputError(BaseInputError):
    def __init__(self):
        msg = 'Invalid score name'
        super().__init__(msg)

class ScoreQuantityInputError(BaseInputError):
    def __init__(self):
        msg = 'Invalid score quantity'
        super().__init__(msg)