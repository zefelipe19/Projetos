import modules

#Esse sistema é um sistema de login com um banco de dados lendo e gravando em um arquivo .txt

database = "Projeto_2_Sistema de Login\data_base.txt"


modules.tituloPrin("Login System in .txt")

user = str(input("User: ")).title().strip()
password = str(input("Password: ")).strip().upper()

modules.leiaArquivo(database, user, password)
