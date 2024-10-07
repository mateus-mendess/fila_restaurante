from colorama import init, Fore, Style
import os

def register_people_view():
        while True:

            os.system("cls||clear")

            print(f"{Fore.LIGHTRED_EX}Galeto Sat's{Style.RESET_ALL} - Fila de espera\n")
            print(f"""Mesa para quantas pessoas ?\n
        {Fore.LIGHTRED_EX}[1]{Style.RESET_ALL} 1 lugar
        {Fore.LIGHTRED_EX}[2]{Style.RESET_ALL} 2 lugares
        {Fore.LIGHTRED_EX}[3]{Style.RESET_ALL} 3 lugares
        {Fore.LIGHTRED_EX}[4]{Style.RESET_ALL} 4 lugares
        {Fore.LIGHTRED_EX}[5]{Style.RESET_ALL} 5+ lugares\n""")
            
            try:
                table_to = int(input("Selecione: "))
            except ValueError:
                continue

            match table_to:
                case 1:
                    table = "1"
                case 2:
                    table = "2"
                case 3:
                    table = "3"
                case 4:
                    table = "4"
                case 5:
                    table = "5+"
                case _:
                    print("Escolha uma opção válida.")
                    continue
            break

        name = str(input("Como podemos te chamar: ")).strip().upper()
        cell_phone = str(input("Número para contato: ")).strip()

        new_person_information = {
            "Nome": name,
            "Telefone": cell_phone,
            "Mesa": table
        }

        return new_person_information