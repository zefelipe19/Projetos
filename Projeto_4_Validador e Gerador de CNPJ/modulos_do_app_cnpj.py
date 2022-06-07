# Esses vão ser os modulos que vão receber as informações dadas no app.py

def remover_Pontuacao(arg):
    removido = arg.replace('.', '')
    removido = removido.replace('/', '')
    removido = removido.replace('-', '')
    return removido


def validador_CNPJ(arg):
    lista_cnpj = arg[:-2]
    multiplicador = 9
    soma_total = 0

    for i in range(25):
        i = 12
        multiplicador = 5
        if len(lista_cnpj) >= 13:
            multiplicador = 6
        
        for i in lista_cnpj:
            soma_total += int(lista_cnpj[i]) * multiplicador
            multiplicador -= 1

            if multiplicador < 2:
                multiplicador = 9



print(remover_Pontuacao('09.248.936/0001-00'))

print(validador_CNPJ(remover_Pontuacao(09248936000100)))





'''09.248.936/0001-00'''
