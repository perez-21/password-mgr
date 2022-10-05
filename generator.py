class Generator():
    
    def __init__(self) -> None:
        self.__length = 10
        self.__toogleSym = False
        self.__toogleLow = True
        self.__toogleUpp = True
        self.__toogleNum = True
        pass
    
    def get_length(self,):
        return self.length

    def is_symbol(self,):
        return self.__toogleSym

    def is_lowercase(self,):
        return self.__toogleLow

    def is_uppercase(self,):
        return self.__toogleUpp

    def is_num(self,):
        return self.__toogleNum


    def set_num(self, value):
        self.__toogleNum = value

    def set_lowercase(self, value):
        self.__toogleLow = value

    def set_uppercase(self, value):
        self.__toogleUpp = value

    def set_sym(self, value):
        self.__toogleSym = value

    def set_length(self, newLength):
        self.__length = newLength

    def __generate(self, symstate ,upperstate ,lowerstate ,numberstate ,length):
    
        password = 'password'
        
        #use setters to do appropriate setting, loll
        

        #generate password


        return password