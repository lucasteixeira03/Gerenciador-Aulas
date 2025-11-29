from .instrutor import Instrutor

class Aula:
    def __init__(self, titulo, descricao=None, instrutor: Instrutor = None, duracao = 0):
        self.titulo = titulo
        self.descricao = descricao
        self.instrutor = instrutor
        self.duracao = duracao

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

    @property
    def duracao(self):
        return self.__duracao
    
    @duracao.setter
    def duracao(self, duracao):
        try:
            duracao = int(duracao)
            if duracao > 0:
                self.__duracao = duracao
            else:
                self.__duracao = "Indeterminado"
        except ValueError:
            self.__duracao = "Indeterminado"
            
    def __str__(self):
        descricao = f"Descrição: {self.descricao}\n" if self.descricao else ""
        instrutor_nome = self.instrutor.nome if self.instrutor else "Nenhum"
        if isinstance(self.duracao, int) and self.duracao > 0:
            duracao = f"Duração: {self.duracao} minutos\n"
        else:
                duracao = "Duração: Indeterminado\n" 
        return f"Aula: {self.titulo}\n{descricao}Instrutor(a): {instrutor_nome}\n{duracao}\n"

    def exibir_dados(self):
        descricao = f"Descrição: {self.descricao}\n" if self.descricao else ""
        instrutor_nome = self.instrutor.nome if self.instrutor else "Nenhum"
        if isinstance(self.duracao, int) and self.duracao > 0:
            duracao = f"Duração: {self.duracao} minutos\n"
        else:
            duracao = "Duração: Indeterminado\n" 
        return f"Aula: {self.titulo}\n{descricao}Instrutor(a): {instrutor_nome}\n{duracao}"