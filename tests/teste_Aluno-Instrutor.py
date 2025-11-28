import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from models.aluno import Aluno
from models.instrutor import Instrutor


print("=== TESTE DE ALUNO E INSTRUTOR ===\n")

aluno = Aluno("  Lucas Teixeira  ", "  lucasteixeira.pf@ifsul.com  ", "  0102025  ")
instrutor = Instrutor("  Vanessa Machado  ", "  vanessa.pf@ifsul.com  ", "  CREF12345  ")

print("-> Testando __str__()")
print(" === Aluno ===")
print(aluno)
     
print("\n === Instrutora ===")
print(instrutor)   

print("\n-> Testando exibir_dados()")
print(aluno.exibir_dados())
print(instrutor.exibir_dados())

print("\n-> Testando setters (strip funcionando)")
aluno.matricula = "   B987   "
instrutor.cref = "   CREF99999   "

print("Matrícula atualizada do aluno:", aluno.matricula)
print("CREF atualizado do instrutor:", instrutor.cref)

print("\n-> Testando atualização de nome e email")
aluno.nome = "   Novo Nome Aluno   "
aluno.email = "   novoemail.pf@ifsul.com   "
instrutor.nome = "   Novo Nome Instrutor   "
instrutor.email = "   novoemail.instrutor@ifsul.com   "

print(aluno.exibir_dados())
print(instrutor.exibir_dados())
