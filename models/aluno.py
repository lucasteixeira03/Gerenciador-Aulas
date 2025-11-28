from .pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, email, matricula):
        super().__init__(nome, email)
        self.matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula.strip()

    def __str__(self):
        return f"{super().__str__()}Matrícula: {self.__matricula}"

    def exibir_dados(self):
        return f"Aluno: {self.nome}\nEmail: {self.email}\nMatrícula: {self.matricula}\n"


    """ Código comentado para evitar bugs no momento
    
    def inscrever(self, sessão: "SessãoAula"):
        return sessão.inscrever(self)""" 