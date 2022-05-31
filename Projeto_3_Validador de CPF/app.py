import modules
print("Validador de CPF")

cpf = (input("Digite um CPF: "))

if modules.cpf_validate(cpf) == True:
    print("CPF Valido")
else:
    print("CPF Invalido")