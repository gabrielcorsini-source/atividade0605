from model.filme import Filme
from repository.filme_repository import FilmeRepository

class FilmeService:

    def __init__(self):
        self.repository = FilmeRepository()

    def criar_usuario(self, titulo, genero, duracao,):
        if titulo == "":
            raise Exception("Titulo obrigatorio")
        



        if duracao <=0:
            raise Exception("Duração invalida")
        
        filme = Filme(titulo, genero, duracao)
        self.repository.salvar(filme)

    def listar_filme(self):
        return self.repository.listar()