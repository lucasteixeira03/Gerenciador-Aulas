from .pessoa import Pessoa

class Instrutor(Pessoa):
    def __init__(self, nome, email, cref):
        super().__init__(nome, email)
        self.cref = cref

    @property
    def cref(self):
        return self.__cref
    
    @cref.setter
    def cref(self, cref):
        self.__cref = cref.strip()

    def __str__(self):
        return f"{super().__str__()}CREF: {self.__cref}"

    def exibir_dados(self):
        return f"Instrutor(a): {self.nome}\nEmail: {self.email}\nCREF: {self.cref}"