from service.filme_service import FilmeService

class FilmeController:
    def __init__(self):
        self.service = FilmeService()

    def criar_filme(self):
        titulo = input("Título: ")
        genero = input("Gênero: ")
        duracao = int(input("Duração: "))

        self.service.criar_filme(titulo, genero, duracao)

        print("Filme cadastrado com sucesso!")

    def listar_filmes(self):
        filmes = self.service.listar_filmes()

        for filme in filmes:
            print(filme)