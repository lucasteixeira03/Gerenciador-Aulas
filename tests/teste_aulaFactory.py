import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from factories.aula_factory import AulaFactory


print("=== TESTE DA AULAFACTORY ===\n")

tipos_aula = [
    "personal trainer",
    "funcional",
    "pilates",
    "musculacao",
    "spinning",
    "yoga",
    "aula desconhecida"
]

for tipo in tipos_aula:
    print(f"-> Criando aula do tipo: '{tipo}'")
    aula = AulaFactory.criar_aula(tipo)
    print(aula.exibir_dados())
    print("-" * 40 + "\n")
