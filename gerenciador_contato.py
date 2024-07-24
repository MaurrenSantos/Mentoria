import csv
def menu_principal():
    while True:
        print ("\nSistema de Gerenciamento de Contatos")
        print("1. Adicionar Contato")
        print("2. Visualizar Contatos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_contato()
        elif opcao == '2':
            vizualizar_contatos()
        elif opcao == '3':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")
#chamando o menu principal
menu_principal()
def adicionar_contato():
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    with open("contatos.csv","a", newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow([nome, telefone, email])
        print("Contato salvo com sucesso!")
def vizualizar_contatos():
    try:
        with open("contatos.csv", "r") as arquivo_csv:
            reader = csv.reader(arquivo_csv)
            print("\nContatos salvos: ")
            for row in reader:
                print(f"Nome: {row[0]}, Telefone: {row[1]}, E-mail: {row[2]}")
    except FileNotFoundError:
        print("Nenhum contato encontrado. Adicione contatos primeiro.")
