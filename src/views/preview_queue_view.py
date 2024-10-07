from colorama import Fore, Style
import os

def preview_queue_view():
    while True:
        os.system("cls||clear")
        
        print(f"""Filas - {Fore.LIGHTRED_EX}Galeto Sat's{Style.RESET_ALL}\n
    {Fore.LIGHTRED_EX}[1]{Style.RESET_ALL} Fila Geral
    {Fore.LIGHTRED_EX}[2]{Style.RESET_ALL} Fila mesa para 1
    {Fore.LIGHTRED_EX}[3]{Style.RESET_ALL} Fila mesa para 2
    {Fore.LIGHTRED_EX}[4]{Style.RESET_ALL} Fila mesa para 3
    {Fore.LIGHTRED_EX}[5]{Style.RESET_ALL} Fila mesa para 4
    {Fore.LIGHTRED_EX}[6]{Style.RESET_ALL} Fila mesa para 5
    {Fore.LIGHTRED_EX}[7]{Style.RESET_ALL} Sair""")
        try:
            command = int(input("Digite uma opção: "))
        except ValueError:
            print("Opção Invalida!")
            continue
        
        return command