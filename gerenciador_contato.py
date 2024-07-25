import csv

def adicionar_contato():
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")

    with open("contatos.csv", "a", newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow([nome, telefone, email])
        print("Contato salvo com sucesso!")
def visualizar_contatos():
    try:
        with open("contatos.csv", "r") as arquivo_csv:
            reader = csv.reader(arquivo_csv)
            print("\nContatos salvos:")
            for row in reader:
                print(f"Nome: {row[0]}, Telefone: {row[1]}, E-mail: {row[2]}")
    except FileNotFoundError:
        print("Nenhum contato encontrado. Adicione contatos primeiro.")
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
            visualizar_contatos()
        elif opcao == '3':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")
#chamando o menu principal
menu_principal()
import re
def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao, email)

def adicionar_contato():
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    while not telefone.isdigit():
        telefone = input ("Telefone inválido. Digite novamente: ")
    email = input("Digite o email: ")
    while not email.isdigit():
        email = input("E-mail inválido. Digite novamente: ")
    with open("contatos.csv", "a", newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow([nome, telefone, email])
    print("Contato adicionado com sucesso!")
def remover_contato():
    nome = input("Digite o nome do contato a ser removido: ")
    contatos = []
    with open("contatos.csv", "r", newline='') as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        contatos = [row for row in reader if row[0] !=nome]
    with open("contatos.csv", "w", newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(contatos)
        print(f"Contato 'nome' removido com sucesso!")
def menu_principal():
    while True:
        print("\nSistema de Gerenciamento de Contatos")
        print("1. Adicionar contato")
        print("2. Visualizar contatos")
        print("3. Remover contato")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_contato()
        elif opcao == '2':
            visualizar_contatos()
        elif opcao == '3':
            remover_contato()
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
def atualizar_contato():
    nome = input("Digite o nome do contato a ser atualizado: ")
    contatos = []
    encontrado = False
    with open("contatos.csv", "r") as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for row in reader:
            if row[0] == [nome]:
                telefone = input ("Digite o novo telefone: ")
                while not telefone.isdigit():
                    telefone = input("Telefone inválido. Digite novamente: ")
                email = input("Digite o novo email: ")
                while not validar_email(email):
                    email = input("E-mail inválido. Digite novamente: ")
                contatos.append([nome, telefone, email])
                encontrado = True
            else:
                contatos.append(row)
            if encontrado:
                with open("contatos.csv", "w", newline='') as arquivo_csv:
                    writer = csv.writer(arquivo_csv)

