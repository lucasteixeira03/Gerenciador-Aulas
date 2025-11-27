from .instrutor import Instrutor

class Aula:
    def __init__(self, titulo, descricao=None, instrutor: Instrutor = None):
        self.titulo = titulo
        self.descricao = descricao
        self.instrutor = instrutor

    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo.strip().title()

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao.strip() if descricao else None

    @property
    def instrutor(self):
        return self._instrutor
    
    @instrutor.setter
    def instrutor(self, instrutor):
        if instrutor is not None and not isinstance(instrutor, Instrutor):
            raise TypeError("Instrutor deve ser um objeto da classe Instrutor.")
        else:
            self._instrutor = instrutor

    def __str__(self):
        descricao = f"Descrição: {self.descricao}\n" if self.descricao else ""
        instrutor_nome = self._instrutor.nome if self._instrutor else "Nenhum"
        return f"Aula: {self.titulo}\n{descricao}Instrutor: {instrutor_nome}"
