from colorama import Fore, Style
import os

def register_employee_view():
    os.system("cls||clear")

    print(f"Cadastrar Funcionário - {Fore.LIGHTRED_EX}Galeto Sas't{Style.RESET_ALL}\n")

    name = str(input("Digite seu nome: ")).strip().upper()
    user = str(input("Digite seu usuario: "))
    password = str(input("Digite sua senha: "))

    register_information = {
        "nome": name,
        "usuario": user,
        "senha": password
    }

    return register_information
