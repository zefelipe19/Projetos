def tituloPrin(msg): # Esse é um modulo de titulo, apenas estético
    print("\033[1m")
    print("-" * 40)
    print(f"{msg.center(40)}")
    print("-" * 40)
    print("\033[m")


def leiaArquivo(NomeArquivo, user, password): # Esse é o sistema que lê o arquivo .txt e transfere para uma lista
    u = user
    p = password
    up = u+p # É essa variável que lê os dados do arquivo .txt
    user_check = []
    with open (NomeArquivo, "rt+") as leia_Arquivo:
        for l in leia_Arquivo:
            user_check.append(l)
        if f"{up}\n" in user_check:
            print(f"Hello! {u}")
        else:
            print("User Not Found!")
            menu = str(input("Want add it? [Y]es | [N]o: ")).upper().strip()[0]
            if menu == "Y":
                escrevaArquivo(NomeArquivo, user, password)


def escrevaArquivo(NomeArquivo, user, password):
    u = user
    p = password
    with open (NomeArquivo, "a+") as escreva_Arquivo:
        escreva_Arquivo.write(f"{u}")
        escreva_Arquivo.write(f"{p}")
        escreva_Arquivo.write("\n")

