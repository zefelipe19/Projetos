''' 94.739.426/0001-05
     21068994000158 '''

MULTIPLICADORES = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

def remove_pontuacao(arg):
    removido = arg.replace('.', '')
    removido = removido.replace('-', '')
    removido = removido.replace('/', '')
    return removido


def is_sequence(arg):
    sequencia = arg[0] * len(arg)
    if sequencia == arg:
        return True
    else:
        return False


def calcula_digitos(cnpj, digito):
    if digito == 1:
        multiplicadores = MULTIPLICADORES[1:]
    elif digito == 2:
        multiplicadores = MULTIPLICADORES



def valida_cnpj(arg):
    original_cnpj = arg

    if is_sequence(arg):
        return False

    novo_cnpj = calcula_digitos(cnpj=cnpj, digito=1)