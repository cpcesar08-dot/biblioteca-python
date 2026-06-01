livros = []

def salvar_livros():
    with open("livros.txt", "w") as arquivo:
        for livro in livros:
            arquivo.write(livro + "\n")

def carregar_livros():
    try:
        with open("livros.txt", "r") as arquivo:
            for linha in arquivo:
                livros.append(linha.strip())

    except FileNotFoundError:
        pass

def adcionar():
    entrada_2 = input("adicione um livro: ")
    livros.append(entrada_2)

    salvar_livros()
    
    print("livro adicionado com sucesso!!!!")


def listar():
    for x in livros:
        livros.sort
        print(x)


def remover():
    entrada = input("digete o nome do livro: ")
    if entrada in livros:
        livros.remove(entrada)
        print("removido com sucesso!!!")
    else:
        print("livro nao encontrado!!!")


def procura():
     entrada = input("digite o livro: ")
     if entrada in livros:
          print("livro encontra!!!")
          print(entrada)
     else:
          print("livro nao encontrado")

        

    
def opcao():
    print("==== MENU ====")
    print("1- adicionar livro")
    print("2- listar livros")
    print("3- remover")
    print("4- busacr livro")
    print("5- sair")

    opcao = input("escolha uma funçao: ")

    if opcao == "1":
        adcionar()
    elif opcao == "2":
            listar()
    elif opcao == "3":
            remover()
    elif opcao == "4":
         procura()

    elif opcao == "5":
            return False   



carregar_livros()

#retorna falso para encerrar o codigo  
while True:   
    resultado = opcao()

    if resultado == False:
        break
