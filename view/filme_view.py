class FilmeView:

    def mostrar_menu(self):
        print("\n" + "="*30)
        print("        MENU FILME")
        print("="*30)
        print("[1] Criar Filme")
        print("[2] Listar Filmes")
        print("[0] Sair")
        print("="*30)

    def obter_dados_filme(self):
        print("\n--- Cadastro de Filme ---")
        titulo= input("Titulo  : ")
        genero = input("Genero : ")
        duracao = input("Duração : ")
        print("-"*30)
        return  titulo, genero, duracao

    def mostrar_filme(self, filme):
        print("\n" + "="*40)
        print("         LISTA DE FILMES")
        print("="*40)

        if not filme:
            print("Nenhum filme cadastrado.")
        else:
            for u in filme:
                print(f"Titulo: {u.titulo}")
                print(f"Genero : {u.genero}")
                print(f"Duração: {u.duracao}")
                print("-"*40)

        print("="*40)

    def mostrar_mensagem(self, mensagem):
        print("\n>> " + mensagem + "\n")