import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from datetime import datetime
from models.aluno import Aluno  
from models.inscricao import Inscricao
from models.enums import StatusInscricao

print("=== TESTE DE INSCRIÇÃO ===\n")

aluno1 = Aluno("  Lucas Teixeira  ", "lucas.teixeira@gmail.com", "0102025")

insc1 = Inscricao(aluno1)
print("-> Inscrição 1 com status padrão e data automática:")
print(insc1.exibir_dados())

insc1.em_espera()
print("\n-> Inscrição 1 após definir como em espera:")
print(insc1.exibir_dados())

insc1.nao_inscrito()
print("\n-> Inscrição 1 após definir como não inscrito:")
print(insc1.exibir_dados())
print("\n" + "-" * 40 + "\n")

print("-> Teste da classe Inscricao com data fornecida e status inicial:")
insc2 = Inscricao(aluno=aluno1, status=StatusInscricao.EM_ESPERA)
print(insc2.exibir_dados())