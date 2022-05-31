'''def validarDigito1(num):
    cpf_teste = num
    cpf_num = cpf_teste.replace(".", "")
    cpf_num = cpf_num.replace("-", "")
    digitos = []
    for n in cpf_num:
        if n.isdigit():
            digitos.append(int(n))
    soma_1 = 0
    c = 10
    for n in digitos:
        soma_1 += n * c
        c -= 1

    digito_1 = 11 - (soma_1 % 11)
    if digito_1 > 11:
        digito_1 = 0
    
    print(digito_1)'''


def cpf_validate(numbers):
    #  Obtém os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in numbers if char.isdigit()]

    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
    #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
    if cpf == cpf[::-1]:
        return False

    #  Valida os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True


'''075.030.983-09'''
'''168.995.350-09'''