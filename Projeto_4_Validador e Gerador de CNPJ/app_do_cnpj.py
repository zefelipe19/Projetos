from modulos_do_app_cnpj import remover_Pontuacao, validador_CNPJ # isso está importando o arquivo mudules.py na pasta
from time import sleep

print('Gerador e Validador de CNPJ')

while True:
    sleep(0.5)
    print('-' * 40)
    print('''Selecione a opção desejada!
    1. Validar um CNPJ
    2. Gerar um CNPJ
    3. Sair do Programa''')

    menu = str(input('-> '))
    while menu not in '123':
        menu = str(input('-> '))
    
    if menu == '1':
        cnpj = str(input('Digite o CNPJ: '))
        validador_CNPJ(cnpj)

    if menu == '2':
        pass
    
    if menu == '3':
        print('OK....')
        sleep(0.5)
        print('< Volte Sempre >')
        break
