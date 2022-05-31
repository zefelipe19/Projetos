# Esse é o modulo que vai receber a string, tranformar em um numero e fazer a validação
def CPFValidator(number):
    cpf_original = number
    novo_cpf = cpf_original[:-2]
    multplicador = 10
    soma_total = 0

    for i in range(19):
        if i > 8:
            i -= 9
        
        soma_total += int(novo_cpf[i]) * multplicador

        multplicador -= 1

        if multplicador < 2:
            multplicador = 11
            digito = 11 - (soma_total % 11)

            if digito > 9:
                digito = 0
            soma_total = 0
            novo_cpf += str(digito)

    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf_original)


    if cpf_original == novo_cpf and not sequencia:
        print(f"o CPF {cpf_original} é válido!")
    else:
        print(f"o CPF {cpf_original} mão é válido!")
