import csv
# Captura de dados de múltiplos usuários
usuarios = []
while True:
    nome = input("Digite seu nome (ou'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    idade = input("Digite sua idade: ")
    usuarios.append([nome, idade])

#Verifica se há dados para serem salvos
if usuarios:
    #Abre o arquivo em modo escrita
    with open ("dados_usuarios.csv", "w", newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        #Escreve o cabeçalho
        writer.writerow(["Nome", "Idade"])
        #Escreve os dados do usuário
        writer.writerow(usuarios)

    print("Dados salvos com sucesso no arquivo CSV!")
else:
    print("Nenhum dado foi capturado.")
    