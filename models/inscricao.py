from datetime import datetime
from .enums import StatusInscricao

class Inscricao:
    def __init__(self,  aluno, data_hora_inscricao = None, status=StatusInscricao.INSCRITO):
        self.aluno = aluno
        self.status = status

        if status == StatusInscricao.INSCRITO:
            if data_hora_inscricao:
                self.data_hora_inscricao = data_hora_inscricao
            else:
                self.data_hora_inscricao = datetime.now()
        else:
            self.data_hora_inscricao = data_hora_inscricao


    @property
    def aluno(self):
        return self.__aluno
    
    @aluno.setter
    def aluno(self, aluno):
        self.__aluno = aluno

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def data_hora_inscricao(self):
        return self.__data_hora_inscricao

    @data_hora_inscricao.setter
    def data_hora_inscricao(self, data):
        if data is None:
            self.__data_hora_inscricao = None
            return

        if isinstance(data, str):
            try:
                self.__data_hora_inscricao = datetime.strptime(data, "%d-%m-%Y")
            except ValueError as e:
                print(f"Data em formato inválido: {e}")
                self.__data_hora_inscricao = None

        elif isinstance(data, datetime):
            self.__data_hora_inscricao = data

        else:
            print("Data inválida")
            self.__data_hora_inscricao = None


    def inscrito(self):
        self.__status = StatusInscricao.INSCRITO
        self.__data_hora_inscricao = datetime.now()

    def em_espera(self):
        self.__status = StatusInscricao.EM_ESPERA
        self.__data_hora_inscricao = None

    def nao_inscrito(self):
        self.__status = StatusInscricao.NAO_INSCRITO
        self.__data_hora_inscricao = None

    def definir_inscrito(self):
        return self.__status == StatusInscricao.INSCRITO

    def definir_em_espera(self):
        return self.__status == StatusInscricao.EM_ESPERA
    
    def definir_nao_inscrito(self):
        return self.__status == StatusInscricao.NAO_INSCRITO
    

    def __str__(self):
        data = f"{self.data_hora_inscricao.strftime('%d-%m-%Y')}" if self.data_hora_inscricao else "Sem data definida"
        return f"{self.aluno}\nStatus: {self.status.value}\nData da Inscrição: {data}"
    
    def exibir_dados(self):
        data = f"{self.data_hora_inscricao.strftime('%d-%m-%Y')}" if self.data_hora_inscricao else "Sem data definida"
        return f"{self.aluno.exibir_dados()}Status: {self.status.value}\nData da Inscrição: {data}\n"