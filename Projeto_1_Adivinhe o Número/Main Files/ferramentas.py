# Modulos usados no jogo
def aleatorio(a, b):
    from random import randint
    ale = randint(a, b)
    return ale


def titulo(msg):
    l = len(msg) + 8
    print("-" * l)
    print(f"    {msg}")
    print("-" * l)


def linha(msg):
    l = len(msg) + 4
    print("-" * l)
    print(f"  {msg}")
    print("-" * l)


def prin(msg):
    l = len(msg) + 50
    print("\033[1;32m")
    print("-" * l)
    print(f"                         {msg}")
    print("-" * l)
    print("\033[m")


def musica():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load(".\Projeto_1_Adivinhe o Número\Lofi.mp3")
    pygame.mixer.music.play()
    

def jogo(inicio, fim):
    if fim == 10:
        dificuldade = "Easy"
    elif fim == 30:
        dificuldade = "Normal"
    elif fim == 50:
        dificuldade = "Hard"
    total_score = 0
    partidas = 0
    while True:
            partidas += 1
            print("\033[1;32m")
            linha(f"Estou pensando em um número entre ({inicio} e {fim})")
            print("Que número é esse?")
            score = fim
            pc = aleatorio(inicio, fim)
            print(f"RESP {pc}")
            player = int(input("-> "))
            print("\033[m")
            while player != pc:
                if player > pc:
                    titulo("\033[1;31mBeh! É menos!\033[m")
                else:
                    titulo("\033[1;31mBeh! É mais!\033[m")
                if score == 0:
                    titulo("\033[1;31mGame Over! Suas chances acabaram!\033[m")
                    break
                score -= 1
                player = int(input("-> "))
            if player == pc:
                print("\033[1;32m")
                print(f"Parabéns você acertou! Meu número era {pc}")
                print(f"Você ganhou {score} pontos!")
                print("\033[1;32m")
            
            total_score += score

            continua = str(input("Quer jogar de novo? [S/N] -> ")).upper().strip()[0]
            while continua not in "SN":
                print("Erro! Por Favor responda apenas com [S/N] -> ")
                cpmtinua = str(input("-> "))
            if continua == "N":
                print("OK")
                break
    banco = open(".\Projeto_1_Adivinhe o Número\pontuacoes.txt", "a")

    if total_score > 0:
        name = str(input("Digite seu nome: ")).title().strip()
        print(f"Sua pontuação é {total_score} pontos!")

        banco.write(f"Nome do Jogador: [{name}]")
        banco.write("\t")
        banco.write(str(f"Total Score: [{total_score}] "))
        banco.write("\t")
        banco.write(f"Dificuldade: [{dificuldade}]")
        banco.write("\t")
        banco.write(f"Number of Times: [{partidas}]")
        banco.write("\n")

