from colorama import init, Style, Fore
import os

def introduction_page():
    init()
    os.system("cls||clear")
    print(f"""Bem-Vindo ao {Fore.LIGHTRED_EX}Galeto Sat's{Style.RESET_ALL}\n
    {Fore.LIGHTRED_EX}[1]{Style.RESET_ALL} Entrar na lista de espera
    {Fore.LIGHTRED_EX}[2]{Style.RESET_ALL} Login Funcionário
    {Fore.LIGHTRED_EX}[8]{Style.RESET_ALL} Sair
    """)
    try:
        command = int(input("Qual serviço você deseja utilizar: "))
    except ValueError:
        print(F"{Fore.LIGHTRED_EX}Serviço não encontrado. Por Favor, Selecione uma opção válida{Style.RESET_ALL}\n")
        exit()
        
    return command