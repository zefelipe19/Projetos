import modulos_do_app_cnpj # isso está importando o arquivo mudules.py na pasta
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
        modulos_do_app_cnpj.validadorCNPJ(modulos_do_app_cnpj.removerPontuacao(cnpj))

    if menu == '2':
        pass
    else:
        print('OK....')
        sleep(0.5)
        print('< Volte Sempre >')
        break
