from service.filme_service import FilmeService

class FilmeController:

    def __init__(self, view):
        self.service = FilmeService()
        self.view = view

    def criar_filme(self):
        titulo, genero, duracao = self.view.obter_dados_filme()
        self.service.criar_usuario(titulo, genero, duracao)
        self.view.mostrar_mensagem("Filme criado com sucesso!")

    def listar_filme(self):
        filme = self.service.listar_filme()
        self.view.mostrar_filme(filme)