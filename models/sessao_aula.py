from datetime import datetime
from .aula import Aula
from .inscricao import Inscricao
from .enums import StatusInscricao


class SessaoAula:
    def __init__(self, aula, data_hora, sala, capacidade):
        self.aula = aula
        self.data_hora = data_hora
        self.sala = sala
        self.capacidade = capacidade
        self.inscricoes = []

    @property
    def aula(self):
        return self.__aula

    @aula.setter
    def aula(self, aula):
        if not isinstance(aula, Aula):
            raise TypeError("aula deve ser um objeto da classe Aula")
        self.__aula = aula

    @property
    def data_hora(self):
        return self.__data_hora

    @data_hora.setter
    def data_hora(self, data_hora):
        if isinstance(data_hora, datetime):
            self.__data_hora = data_hora
        elif isinstance(data_hora, str):
            try:
                self.__data_hora = datetime.strptime(data_hora, "%d-%m-%Y %H:%M")
            except ValueError as e:
                print("Data/Hora inválida (use dd-mm-YYYY HH:MM):", e)
                self.__data_hora = None
        else:
            print("Valor inválido para data_hora.")
            self.__data_hora = None

    @property
    def sala(self):
        return self.__sala
    
    @sala.setter
    def sala(self, sala):
        if sala is None:
            self.__sala = ""
        else:
            self.__sala = str(sala).strip().title()

    @property
    def capacidade(self):
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, valor):
        try:
            valor = int(valor)
            if valor < 0:
                print("Capacidade não pode ser negativa!")
                valor = 0
            self.__capacidade = valor
        except (ValueError, TypeError):
            print("Capacidade inválida!")
            self.__capacidade = 0

    @property
    def inscricoes(self):
        return self.__inscricoes
    
    @inscricoes.setter
    def inscricoes(self, inscricoes):
        self.__inscricoes = inscricoes
    

    def vagas_disponiveis(self):
        inscritos = 0
        for insc in self.__inscricoes:
            if insc.status == StatusInscricao.INSCRITO:
                inscritos += 1

        return self.capacidade - inscritos
    
    def total_inscritos(self):
        return len([insc for insc in self.__inscricoes if insc.status == StatusInscricao.INSCRITO])
    
    def total_em_espera(self):
        return len([insc for insc in self.__inscricoes if insc.status == StatusInscricao.EM_ESPERA])
    
    def inscrever(self, aluno):

        if self.vagas_disponiveis() > 0:
            inscricao = Inscricao(aluno, status=StatusInscricao.INSCRITO)
        else:
            inscricao = Inscricao(aluno, status=StatusInscricao.EM_ESPERA)

        self.__inscricoes.append(inscricao)
        return inscricao

    def listar_inscritos(self):
        return [i.aluno for i in self.__inscricoes if i.status == StatusInscricao.INSCRITO]

    def listar_em_espera(self):
        return [i.aluno for i in self.__inscricoes if i.status == StatusInscricao.EM_ESPERA]
    
    def __str__(self):
        return self.exibir_dados()

    def exibir_dados(self):
        data_hora = (self.data_hora.strftime("%d-%m-%Y (%H:%M)")) if self.data_hora else "Sem data definida"
        professor = self.aula.instrutor.nome if self.aula.instrutor else "Nenhum"
        if isinstance(self.aula.duracao, int) and self.aula.duracao > 0:
            duracao = f"{self.aula.duracao} minutos"
        else:
            duracao = "Indeterminado"
            
        return (f"Sessão da Aula:\n"
                f"Aula: {self.aula.titulo}\n"
                f"Instrutor(a): {professor}\n"
                f"Data e Hora: {data_hora}\n"
                f"Duração: {duracao}\n"  
                f"Sala: {self.sala}\n"
                f"Capacidade: {self.capacidade}\n"
                f"Vagas Disponíveis: {self.vagas_disponiveis()}\n"
                f"Total Inscritos: {self.total_inscritos()}\n"
                f"Total em Espera: {self.total_em_espera()}\n")
    