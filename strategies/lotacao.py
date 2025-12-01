from abc import ABC, abstractmethod
from models.enums import StatusInscricao

# classe base para diferentes estratégias de ocupação (SessãoAula)
class EstrategiaLotacao(ABC):

    # recebe um objeto SessaoAula e retorna um StatusInscricao
    @abstractmethod
    def definir_status_inscricao(self, sessao_aula):
        pass


class EstrategiaLotacaoPadrao(EstrategiaLotacao):

    def definir_status_inscricao(self, sessao_aula):
        if sessao_aula.vagas_disponiveis() > 0:
            return StatusInscricao.INSCRITO
        return StatusInscricao.EM_ESPERA


class EstrategiaLotacaoSemEspera(EstrategiaLotacao):
    
    def definir_status_inscricao(self, sessao_aula):
        if sessao_aula.vagas_disponiveis() > 0:
            return StatusInscricao.INSCRITO
        return StatusInscricao.NAO_INSCRITO
