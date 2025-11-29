from models.aula import Aula
from models.instrutor import Instrutor

class AulaFactory:

    @staticmethod
    def criar_aula(tipo):
        tipo_aula = tipo.strip().lower()

        # criando instrutores 
        instrutores_padrao = {
            "personal trainer": Instrutor("Rafael Lopes", "rafael.lopes@academia.com", "CREF11111"),
            "funcional": Instrutor("Cleber Machado", "cleber.machado@academia.com", "CREF22222"),
            "pilates": Instrutor("Cris Colombeli", "cris.colombeli@academia.com", "CREF33333"),
            "musculacao": Instrutor("Tayron Silva", "tayron.silva@academia.com", "CREF44444"),
            "spinning": Instrutor("Sueli Teixeira", "sueli.teixeira@academia.com", "CREF55555"),
            "yoga": Instrutor("Vanessa Machado", "vanessa.machado@academia.com", "CREF12345"),
        }

        instrutor = instrutores_padrao.get(tipo_aula, Instrutor("Inexistente", "inexistente@academia.com", "CREF00000"))

        if tipo_aula == "personal trainer":
            titulo = "Personal Trainer"
            descricao = "Aula individualizada com foco em objetivos específicos."
            duracao = 60

        elif tipo_aula == "funcional":
            titulo = "Funcional em grupo"
            descricao = "Aula de treinamento funcional para grupos."
            duracao = 45

        elif tipo_aula == "pilates":
            titulo = "Pilates"
            descricao = "Aula para ajuste de postura e equilíbrio."
            duracao = 60

        elif tipo_aula == "musculacao":
            titulo = "Musculação Livre"
            descricao = "Musculação com equipamentos variados."
            duracao = "INDEFINIDO"

        elif tipo_aula == "spinning":
            titulo = "Spinning"
            descricao = "Aula de ciclismo indoor com música animada."
            duracao = 45

        elif tipo_aula == "yoga":
            titulo = "Yoga"
            descricao = "Aula focada em alongamento e respiração."
            duracao = 30

        else:
            titulo = tipo.title()
            descricao = "Aula genérica cadastrada pela academia."
            duracao = 60

        return Aula(titulo, descricao, instrutor, duracao)