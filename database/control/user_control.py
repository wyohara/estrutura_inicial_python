from ..models.user_model import UserModel

"""
Controle geral de banco de dados

Ciado por Willian Ohara
09/12/2024
"""

def main():
    db_file = "users.db"
    user_model = UserModel(db_file)

    while True:
        print("\n1. Criar usuário")
        print("2. Ler usuários")
        print("3. Atualizar usuário")
        print("4. Deletar usuário")
        print("5. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            name = input("Nome: ")
            age = int(input("Idade: "))
            user_id = user_model.create_user(name, age)
            print(f"Usuário criado com ID: {user_id}")

        elif choice == '2':
            users = user_model.read_users()
            print("Usuários:")
            for user in users:
                print(user)

        elif choice == '3':
            user_id = int(input("ID do usuário a ser atualizado: "))
            name = input("Novo nome: ")
            age = int(input("Nova idade: "))
            user_model.update_user(user_id, name, age)
            print("Usuário atualizado.")

        elif choice == '4':
            user_id = int(input("ID do usuário a ser deletado: "))
            user_model.delete_user(user_id)
            print("Usuário deletado.")

        elif choice == '5':
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
