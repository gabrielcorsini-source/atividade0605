from model.filme import Filme
from repository.filme_repository import FilmeRepository

class FilmeService:
    def __init__(self):
        self.repository = FilmeRepository()

    def criar_filme(self, titulo, genero, duracao):
        filme = Filme(titulo, genero, duracao)
        self.repository.salvar(filme)

    def listar_filmes(self):
        return self.repository.listar()