class Generator():
    
    def __init__(self) -> None:
        self._length = 10
        self._toogleSym = False
        self._toogleLow = True
        self._toogleUpp = True
        self._toogleNum = True
        pass
    
    def get_length(self,):
        return self.length

    def is_symbol(self,):
        return self._toogleSym

    def is_lowercase(self,):
        return self._toogleLow

    def is_uppercase(self,):
        return self._toogleUpp

    def is_num(self,):
        return self._toogleNum


    def set_num(self, value):
        self._toogleNum = value

    def set_lowercase(self, value):
        self._toogleLow = value

    def set_uppercase(self, value):
        self._toogleUpp = value

    def set_sym(self, value):
        self._toogleSym = value

    def set_length(self, newLength):
        self._length = newLength