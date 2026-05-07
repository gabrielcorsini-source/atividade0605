from controller.filme_controller import FilmeController

def main():
    controller = FilmeController()

    while True:
        print("\n1 - Cadastrar Filme")
        print("2 - Listar Filmes")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            controller.criar_filme()

        elif opcao == "2":
            controller.listar_filmes()

        elif opcao == "0":
            break

        else:
            print("Opção inválida!")

main()