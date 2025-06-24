usuarios = []

def cadastrar_usuario():
    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")
    usuarios.append({"nome": nome, "email": email})
    print("Usuário cadastrado com sucesso!\n")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.\n")
        return
    print("\nLista de usuários:")
    for i, usuario in enumerate(usuarios):
        print(f"{i+1}. Nome: {usuario['nome']}, E-mail: {usuario['email']}")
    print()

def editar_usuario():
    listar_usuarios()
    try:
        indice = int(input("Digite o número do usuário que deseja editar: ")) - 1
        if 0 <= indice < len(usuarios):
            nome = input("Novo nome: ")
            email = input("Novo e-mail: ")
            usuarios[indice] = {"nome": nome, "email": email}
            print("Usuário editado com sucesso!\n")
        else:
            print("Índice inválido.\n")
    except ValueError:
        print("Entrada inválida.\n")

def excluir_usuario():
    listar_usuarios()
    try:
        indice = int(input("Digite o número do usuário que deseja excluir: ")) - 1
        if 0 <= indice < len(usuarios):
            usuarios.pop(indice)
            print("Usuário excluído com sucesso!\n")
        else:
            print("Índice inválido.\n")
    except ValueError:
        print("Entrada inválida.\n")

def menu():
    while True:
        print("1. Cadastrar usuário")
        print("2. Listar usuários")
        print("3. Editar usuário")
        print("4. Excluir usuário")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            editar_usuario()
        elif opcao == "4":
            excluir_usuario()
        elif opcao == "5":
            break
        else:
            print("Opção inválida.\n")

if __name__ == "__main__":
    menu()