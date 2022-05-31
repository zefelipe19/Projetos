import ferramentas

name = " "
partidadas = 0

ferramentas.musica()

ferramentas.prin("Advinhe o número!")

print("\033[1;32mGostaria de Jogar? [S/N]")
menu0 = str(input("-> ")).strip().upper()[0]

while menu0 not in "SN":
    menu0 = str(input("-> ")).strip().upper()[0]

if menu0 == "S":
    print("Ótimo")
    print('''\033[1mEscolha uma dificuldade:
    -----------\033[m
    \033[1;32m1. Fácil (Easy)\033[m
    \033[1;33m2. Médio (Normal)\033[m
    \033[1;31m3. Difícil (Hard)\033[m''')
    menu1 = int(input("-> "))

    if menu1 == 1:
        ferramentas.jogo(1, 10)

    elif menu1 == 2:
        ferramentas.jogo(1, 30)

    elif menu1 == 3:
        ferramentas.jogo(1, 50)

else:
    print("OK")
