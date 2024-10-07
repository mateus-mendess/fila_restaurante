from src.models.repository.person_repository import person_repository
from tabulate import tabulate
from colorama import Fore, Style
import os

class ServedPeopleController:
    def served(self):
        try:
            if self.__person_served_general():
                self.__person_served_next()

                input("\nPressione enter para voltar...")
        except Exception as exception:
            print(str(exception))

    def __person_served_general(self):
        os.system("cls||clear")

        person_served_general = person_repository.served_person()
        if person_served_general == False:
            print(f"{Fore.LIGHTRED_EX}\nFila geral vazia.{Style.RESET_ALL}")
            input("\nPressione enter para voltar...")
            return False

        person_served_now = [
        ["Celular", "Nome", "Mesa para"],
        [person_served_general.cell_phone, person_served_general.name, person_served_general.table_to]]

        print(f"{Fore.LIGHTRED_EX}Cliente atendido:{Style.RESET_ALL}\n")

        print(tabulate(person_served_now, headers="firstrow", tablefmt="grid"))

        return True
    
    def __person_served_next(self):
        person_general_next = person_repository.person_served_next()
        if person_general_next == False:
            print(f"{Fore.LIGHTRED_EX}\nFila geral vazia.{Style.RESET_ALL}")
            return False

        person_served_next = [
        ["Celular", "Nome", "Mesa para"],
        [person_general_next.cell_phone, person_general_next.name, person_general_next.table_to]]

        print(f"\n{Fore.LIGHTRED_EX}Próximo cliente:{Style.RESET_ALL}\n")

        print(tabulate(person_served_next, headers="firstrow", tablefmt="grid"))
    

