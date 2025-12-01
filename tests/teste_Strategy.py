import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from datetime import datetime
from models.instrutor import Instrutor
from models.aula import Aula
from models.aluno import Aluno
from models.sessao_aula import SessaoAula
from models.enums import StatusInscricao
from strategies.lotacao import EstrategiaLotacaoSemEspera

##########################################
# TESTE COM ESTRATÉGIA SEM FILA DE ESPERA#
##########################################

# Criar instrutor
instrutor = Instrutor("Vanessa Machado", "vanessa.pf@ifsul.com", "CREF12345")
print(instrutor.exibir_dados() + "\n")

# Criando uma aula
aula = Aula("Yoga", "Aula focada em alongamento e respiração", instrutor, 60)
print(aula.exibir_dados())

# Criando alguns alunos
aluno1 = Aluno("  Lucas Teixeira  ", "lucas.teixeira@gmail.com", "0102025")
aluno2 = Aluno("  Gabriel Tanabe  ", "gabriel.tanabe@gmail.com", "0012025")
aluno3 = Aluno("  Gabriel Duarte  ", "gabriel.duarte@gmail.com", "0082024")
aluno4 = Aluno("  Dennis Oliveira  ", "dennis.oliveira@gmail.com", "0122023")

alunos = [aluno1, aluno2, aluno3, aluno4]

print("=== TESTE DE SESSÃO DE AULA (ESTRATÉGIA SEM ESPERA) ===\n")

sessao_sem_espera = SessaoAula(
    aula=aula,
    data_hora="01-12-2025 19:00",
    sala="sala 2",
    capacidade=2,
    estrategia_lotacao=EstrategiaLotacaoSemEspera()
)

print(sessao_sem_espera.exibir_dados())
print("-" * 40 + "\n")

print("-> Realizando inscrições na sessão (estratégia SEM ESPERA)")
inscricoes_sem_espera = []
for a in alunos:
    insc = sessao_sem_espera.inscrever(a)
    inscricoes_sem_espera.append(insc)
    print(f"Inscrição criada para {a.nome}:")
    print(insc.exibir_dados())

print("=" * 40 + "\n")
print("RESUMO DA SESSÃO APÓS INSCRIÇÕES:")
print(sessao_sem_espera.exibir_dados())

print("Alunos INSCRITOS:")
for insc in inscricoes_sem_espera:
    if insc.status == StatusInscricao.INSCRITO:
        print(f"- {insc.aluno.nome}")
print()

print("Alunos NÃO INSCRITOS:")
for insc in inscricoes_sem_espera:
    if insc.status == StatusInscricao.NAO_INSCRITO:
        print(f"- {insc.aluno.nome}")
print()

print(f"Vagas disponíveis na sessão: {sessao_sem_espera.vagas_disponiveis()}")
print("\n" + "=" * 40 + "\n")

print("DETALHES DAS INSCRIÇÕES:")
for insc in inscricoes_sem_espera:
    print(insc.exibir_dados())