import modules_app_cpf
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
        cpf = str(input("Digite o CPF: "))
        modules_app_cpf.CPFValidator(modules_app_cpf.removerPontuacao(cpf))

    elif menu  == "2":
        modules_app_cpf.CPFGenerator()

    elif menu == "3":
        print("OK...")
        sleep(0.5)
        print("< Volte Sempre! >")
        break
