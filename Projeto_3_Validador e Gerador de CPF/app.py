import modules
from time import sleep

print("Gerador e Validador de CPF")

while True:
    sleep(0.5)
    print("-" * 40)
    print("""Selecione o que deseja fazer!
    1. Validar um CPF
    2. Gerar um CPF
    3. Sair do Programa""")

    menu = str(input("-> "))
    while menu not in "123":
        menu = str(input("-> "))
    
    if menu == "1":
        cpf = str(input("Digite o CPF (sem pontuações): "))
        modules.CPFValidator(cpf)

    elif menu  == "2":
        modules.CPFGenerator()

    elif menu == "3":
        print("OK...")
        sleep(0.5)
        print("< Volte Sempre! >")
        break
