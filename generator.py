import random

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
        self.__length = newLength if newLength > 2 else 6

    def generate(self, symstate ,upperstate ,lowerstate ,numberstate ,newLength):
        
        if (newLength < 2 or not upperstate or not symstate or not lowerstate or not numberstate):
            return 'error'
            
        
        password = ''
        
        self.set_length(newLength)
        self.set_lowercase(lowerstate)
        self.set_uppercase(upperstate)
        self.set_num(numberstate)
        self.set_sym(symstate)
        
        symbols = [35, 36, 37, 38, 42, 64, 94]
        uppercase = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]
        lowercase = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121]
        number = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
        main = []
        
        #add needed characters
        main += symbols if self.is_symbol() else []
        main += uppercase if self.is_uppercase() else []
        main += lowercase if self.is_lowercase() else []
        main += number if self.is_num() else []
        
        #generate password
        while len(password) < self.__length :
            c = random.randint(33, 122)  
            if c not in main:
                continue
            password += chr(c)

        return password