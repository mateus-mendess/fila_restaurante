from colorama import Fore, Style
import os

def login_employee_view():
    os.system("cls||clear")
    
    print(f"{Fore.LIGHTRED_EX}Login - Funcionário:{Style.RESET_ALL}\n")
    
    user = str(input("Digite seu usuario: "))
    password = str(input("Digite sua senha: "))

    login_information = {
        "usuario": user,
        "senha": password
    }

    return login_information
