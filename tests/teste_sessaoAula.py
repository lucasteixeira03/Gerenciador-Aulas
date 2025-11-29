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

print ("=== TESTE DE SESSÃO DE AULA ===\n")

# Criar instrutor
instrutor = Instrutor("Vanessa Machado", "vanessa.pf@ifsul.com", "CREF12345")
print(instrutor.exibir_dados())
print("\n" + "-" * 40 + "\n")

# Criando uma aula
aula = Aula("Yoga", "Aula focada em alongamento e respiração", instrutor, 60)
print(aula)
print("-" * 40 + "\n")

# Criando uma sessão de aula
sessao = SessaoAula(aula=aula, data_hora="30-11-2025 18:30", sala="sala 1", capacidade=2)
print(sessao.exibir_dados())
print("-" * 40 + "\n")

# Criando alguns alunos
aluno1 = Aluno("  Lucas Teixeira  ", "lucas.teixeira@gmail.com", "0102025")
aluno2 = Aluno("  Gabriel Tanabe  ", "gabriel.tanabe@gmail.com", "0012025")
aluno3 = Aluno("  Gabriel Duarte  ", "gabriel.duarte@gmail.com", "0082024")
aluno4 = Aluno("  Dennis Oliveira  ", "dennis.oliveira@gmail.com", "0122023")

alunos = [aluno1, aluno2, aluno3, aluno4]

# Inscrevendo alunos na sessão
print("-> Realizando inscrições na sessão...")
inscricoes = []
for a in alunos:
    insc = sessao.inscrever(a)
    inscricoes.append(insc)
    print(f"Inscrição criada para {a.nome}:")
    print(insc.exibir_dados())

print("=" * 40 + "\n")
print("RESUMO DA SESSÃO APÓS INSCRIÇÕES:")
print(sessao.exibir_dados())

# Listando inscritos e em espera
print("Alunos INSCRITOS:")
for a in sessao.listar_inscritos():
    print(f"- {a.nome}")
print()

print("Alunos EM ESPERA:")
for a in sessao.listar_em_espera():
    print(f"- {a.nome}")
print()

print(f"Vagas disponíveis na sessão: {sessao.vagas_disponiveis()}")
print("\n" + "=" * 40 + "\n")

# Só para conferir: mostrar status e data de cada inscrição
print("DETALHES DE CADA INSCRIÇÃO:")
for insc in inscricoes:
    print(insc.exibir_dados())