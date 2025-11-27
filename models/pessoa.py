from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome.strip()

    @property
    def email(self):
        return self._email  

    @email.setter
    def email(self, email):
        self._email = email.strip()

    @abstractmethod
    def exibir_dados(self):
        pass

    def __str__(self):
        return f"Nome: {self._nome}, Email: {self._email}"