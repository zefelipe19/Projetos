# Esses vão ser os modulos que vão receber as informações dadas no app.py

def remover_Pontuacao(arg):
    removido = arg.replace('.', '')
    removido = removido.replace('/', '')
    removido = removido.replace('-', '')
    return removido


def is_sequencia(arg):
    numero = remover_Pontuacao(arg)
    sequencia = numero[0] * len(numero)

    if sequencia == numero:
        return True
    else:
        return False


def validador_CNPJ(arg):

    if is_sequencia(arg):
        print('Esse número é uma sequência.')
        return False
    
    original_cnpj = remover_Pontuacao(arg[:-2])
    novo_cnpj = original_cnpj

    multiplcador = 5
    soma_total = i = 0

    while True:
        
        soma_total += int(novo_cnpj[i]) * multiplcador
        i += 1
        multiplcador -= 1

        if multiplcador < 2:
            multiplcador = 9

        if i == 12 and len(novo_cnpj) == 12:
            digito = 11 - (soma_total % 11)
            if digito > 9:
                digito = 0
            novo_cnpj += str(digito)
            i = digito = 0
            multiplcador = 6
        
        if i == 13 and len(novo_cnpj) == 13:
            digito = 11 - (soma_total % 11)
            if digito > 9:
                digito = 0
            novo_cnpj += str(digito)
            break
    
    print(f'O CNPJ que você digitou foi {remover_Pontuacao(arg)}')
    print(f'O calculado foi {novo_cnpj}')

    if novo_cnpj == remover_Pontuacao(arg):
        print('É válido')
    else:
        print('Não é válido')