from .instrutor import Instrutor

class Aula:
    def __init__(self, titulo, descricao=None, instrutor: Instrutor = None):
        self.titulo = titulo
        self.descricao = descricao
        self.instrutor = instrutor

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo.strip().title()

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao.strip() if descricao else None

    @property
    def instrutor(self):
        return self.__instrutor
    
    @instrutor.setter
    def instrutor(self, instrutor):
        if instrutor is not None and not isinstance(instrutor, Instrutor):
            raise TypeError("Instrutor deve ser um objeto da classe Instrutor.")
        else:
            self.__instrutor = instrutor

    def __str__(self):
        descricao = f"Descrição: {self.descricao}\n" if self.descricao else ""
        instrutor_nome = self.__instrutor.nome if self.__instrutor else "Nenhum"
        return f"Aula: {self.__titulo}\n{descricao}Instrutor(a): {instrutor_nome}"

    def exibir_dados(self):
        descricao = f"Descrição: {self.descricao}\n" if self.descricao else ""
        instrutor_info = self.instrutor.exibir_dados() if self.instrutor else "Instrutor(a): Nenhum"
        return f"Aula: {self.titulo}\n{descricao}{instrutor_info}"