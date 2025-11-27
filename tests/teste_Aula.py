import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from models.instrutor import Instrutor
from models.aula import Aula

print("=== TESTE DE AULA E INSTRUTOR ===\n")

instrutor = Instrutor("Vanessa Machado", "vanessa.pf@ifsul.com", "CREF12345")
aula1 = Aula("Personal Solo", "Aula de treinamento personalizado", instrutor)

print("-> Aula  1 (com instrutor):")
print(aula1)

aula2 = Aula ("Funcional em Grupo", None, None)

print("\n-> Aula 2 (sem descrição e sem instrutor):")
print(aula2)

# Testando setters
aula2.titulo = "   musculação pesada   "
aula2.descricao = "   Treino focado em hipertrofia.   "

instrutor = Instrutor("Gabriel Tanabe", "gabriel.tanabe@ifsul.com", "CREF67890")
aula2.instrutor = instrutor

print("\n-> Aula 2 após atualizar dados:")
print(aula2)

print("\n-> Teste de erro ao passar um instrutor inválido:")
try:
    aula_errada = Aula("Spinning", "Intensivo com summerhits", "Lucas (string)")
except TypeError as e:
    print("OK, erro capturado:", e)