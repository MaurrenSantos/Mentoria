#Captura de dados do usuário
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
#Abre o arquivo em modo de escrita
with open("dados_usuario.txt", "w") as arquivo:
          #Escreve os dados capturados do arquivo
          arquivo.write(f"Nome: {nome}\n")
          arquivo.write(f"Idade: {idade}\n")
print("Dados salvos com sucesso!")
with open ("dados_usuario.txt", "r") as arquivo:
        #Lê o conteúdo do arquivo
        conteudo = arquivo.read()
#Exibe o conteúdo lido
print("Conteúdo do arquivo:")
print(conteudo)