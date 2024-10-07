from colorama import Fore, Style
import os

def functions_employee_view():
    while True:
        os.system("cls||clear")

        print(f"""{Fore.LIGHTRED_EX}Aba - Funcionário:\n{Style.RESET_ALL}
{Fore.LIGHTRED_EX}[1]{Style.RESET_ALL}- Cadastrar funcionário
{Fore.LIGHTRED_EX}[2]{Style.RESET_ALL}- Atender cliente
{Fore.LIGHTRED_EX}[3]{Style.RESET_ALL}- Exibir filas de cliente
{Fore.LIGHTRED_EX}[8]{Style.RESET_ALL}- Sair\n""")
        try:
            command = int(input("Selecione uma opção: "))
        except ValueError:
            break

        return command