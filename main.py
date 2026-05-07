from controller.filme_controller import FilmeController
from view.filme_view import FilmeView

def main():
    view = FilmeView()
    controller = FilmeController(view)

    while True:
        view.mostrar_menu()
        opcao = input("Opção: ")

        if opcao == "1":
            controller.criar_filme()
        elif opcao == "2":
            controller.listar_filme()
        elif opcao == "0":
            break
        else:
            view.mostrar_mensagem("Opção inválida")

if __name__ == "__main__":
    main()