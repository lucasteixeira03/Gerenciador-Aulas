from .pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, email, matricula):
        super().__init__(nome, email)
        self.matricula = matricula

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula.strip()

    def __str__(self):
        return f"{super().__str__()}, Matrícula: {self._matricula}"

    def exibir_dados(self):
        return f"Aluno: {self.nome}, Email: {self.email}, Matrícula: {self.matricula}"


    """ Código comentado para evitar bugs no momento
    
    def inscrever(self, sessão: "SessãoAula"):
        return sessão.inscrever(self)""" 