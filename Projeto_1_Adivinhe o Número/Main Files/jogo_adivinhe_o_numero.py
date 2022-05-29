import ferramentas

name = " "
total_score = 0
dificuldade = " "
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
    \033[1;32m1. Fácil\033[m
    \033[1;33m2. Médio\033[m
    \033[1;31m3. Difícil\033[m''')
    menu1 = int(input("-> "))

    if menu1 == 1:
        dificuldade = "Fácil"
        while True:
            partidadas += 1
            print("\033[1;32m")
            ferramentas.linha("Estou pensando em um número entre (1 e 10)")
            print("Que número é esse?")
            score = 10
            pc = ferramentas.aleatorio(1, 10)
            #print(f"RESP {pc}")
            player = int(input("-> "))
            print("\033[m")
            while player != pc:
                if player > pc:
                    ferramentas.titulo("\033[1;31mBeh! É menos!\033[m")
                else:
                    ferramentas.titulo("\033[1;31mBeh! É mais!\033[m")
                if score == 0:
                    ferramentas.titulo(
                        "\033[1;31mGame Over! Suas chances acabaram!\033[m")
                    break
                score -= 1
                player = int(input("-> "))
            if player == pc:
                print("\033[1;32m")
                print(f"Parabéns você acertou! Meu número era {pc}")
                print(f"Você ganhou {score} pontos!")
                print("\033[1;32m")
            total_score += score
            continua = str(
                input("Quer jogar de novo? [S/N] -> ")).upper().strip()[0]
            while continua not in "SN":
                print("Erro! Por Favor responda apenas com [S/N] -> ")
            if continua == "N":
                print("OK")
                break

    if menu1 == 2:
        dificuldade = "Médio"
        while True:
            partidadas += 1
            print("\033[1;32m")
            ferramentas.linha("Estou pensando em um número entre (1 e 30)")
            print("Que número é esse?")
            score = 30
            pc = ferramentas.aleatorio(1, 30)
            #print(f"RESP {pc}")
            player = int(input("-> "))
            print("\033[m")
            while player != pc:
                if player > pc:
                    ferramentas.titulo("\033[1;31mBeh! É menos!\033[m")
                else:
                    ferramentas.titulo("\033[1;31mBeh! É mais!\033[m")
                if score == 0:
                    ferramentas.titulo(
                        "\033[1;31mGame Over! Suas chances acabaram!\033[m")
                    break
                score -= 1
                player = int(input("-> "))
            if player == pc:
                print("\033[1;32m")
                print(f"Parabéns você acertou! Meu número era {pc}")
                print(f"Você ganhou {score} pontos!")
                print("\033[1;32m")
            total_score += score
            continua = str(
                input("Quer jogar de novo? [S/N] -> ")).upper().strip()[0]
            while continua not in "SN":
                print("Erro! Por Favor responda apenas com [S/N] -> ")
            if continua == "N":
                print("OK")
                break

    if menu1 == 3:
        dificuldade = "Dificíl"
        while True:
            partidadas += 1
            print("\033[1;32m")
            ferramentas.linha("Estou pensando em um número entre (1 e 50)")
            print("Que número é esse?")
            score = 50
            pc = ferramentas.aleatorio(1, 50)
            #print(f"RESP {pc}")
            player = int(input("-> "))
            print("\033[m")
            while player != pc:
                if player > pc:
                    ferramentas.titulo("\033[1;31mBeh! É menos!\033[m")
                else:
                    ferramentas.titulo("\033[1;31mBeh! É mais!\033[m")
                if score == 0:
                    ferramentas.titulo(
                        "\033[1;31mGame Over! Suas chances acabaram!\033[m")
                    break
                score -= 1
                player = int(input("-> "))
            if player == pc:
                print("\033[1;32m")
                print(f"Parabéns você acertou! Meu número era {pc}")
                print(f"Você ganhou {score} pontos!")
                print("\033[1;32m")
            total_score += score
            continua = str(
                input("Quer jogar de novo? [S/N] -> ")).upper().strip()[0]
            while continua not in "SN":
                print("Erro! Por Favor responda apenas com [S/N] -> ")
            if continua == "N":
                print("OK")
                break

else:
    print("OK")

banco = open("pontuacoes.txt", "a")

if total_score > 0:
    name = str(input("Digite seu nome: ")).title().strip()
    print(f"Sua pontuação é {total_score} pontos!")

    banco.write(f"Nome do Jogaor: [{name}]")
    banco.write("\t")
    banco.write(str(f"Pontuação total: [{total_score}] pontos"))
    banco.write("\t")
    banco.write(f"Dificuldade: [{dificuldade}]")
    banco.write("\t")
    banco.write(f"Número de partidas: [{partidadas}]")
    banco.write("\n")
