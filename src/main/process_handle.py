from  src.main.constructor.introduction_process import introduction_process
from src.main.constructor.people_register_constructor import people_register_constructor
from src.main.constructor.login_employee_constructor import login_employee_constructor
from src.main.constructor.functions_employee_constructor import functions_employee_constructor
from colorama import init, Fore, Style
def start():
    while True:
        command = introduction_process()

        match command:
            case 1:
                people_register_constructor()
            case 2:
                if login_employee_constructor():
                    functions_employee_constructor()
                continue
            case 8:
                print(f"{Fore.LIGHTRED_EX}Obrigado!{Style.RESET_ALL} Você é sempre bem-vindo.\n")
                exit()
            case _:
                print(F"{Fore.LIGHTRED_EX}Serviço não encontrado. Por Favor, Selecione uma opção válida{Style.RESET_ALL}\n")
                input("Pressione enter para continuar...")
                continue