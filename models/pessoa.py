from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome.strip()

    @property
    def email(self):
        return self.__email  

    @email.setter
    def email(self, email):
        self.__email = email.strip()

    @abstractmethod
    def exibir_dados(self):
        pass

    def __str__(self):
        return f"Nome: {self.__nome}\nEmail: {self.__email}\n"