from src.models.repository.person_repository import person_repository
from tabulate import tabulate
from colorama import Fore, Style
import os

class PreviewQueueController:
    def preview(self, command):
        try:
            if self.__format_response(command):

                input("\nPressione enter para voltar...")
        except Exception as exception:
            print(str(exception))

    def __format_response(self, command):
        os.system("cls||clear")

        dados = person_repository.preview_queue_general(command)

        if dados == 7:
            return False
        
        elif dados == False:
            print(f"{Fore.LIGHTRED_EX}Fila Vazia!{Style.RESET_ALL}\n")
            return True
        else:
            print(tabulate(dados, headers=["Celular", "Nome", "Mesa para"], tablefmt="grid"))
            return True

