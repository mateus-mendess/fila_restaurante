from src.models.repository.person_repository import person_repository
from src.models.entities.person import Person
from colorama import Fore, Style
from datetime import datetime
import os, keyboard

class PeopleRegisterController:

    def register_people(self, new_person_information: dict):
        try:
            if self.__check_name(new_person_information):
                self.__create_person_entity(new_person_information)
                self.__format_response()
            else:
                input("Pressione enter para voltar...")
        except Exception as exception:
            print(str(exception))

    def __check_name(self, new_person_information):
        name_person = new_person_information ["Nome"]
        
        if not name_person.replace(" ", "").isalpha():
            print(f"{Fore.LIGHTRED_EX}Nome incorreto.{Style.RESET_ALL}")
            return False
        try: int(new_person_information["Telefone"])
        except ValueError:
            print(f"{Fore.LIGHTRED_EX}Telefone Inválido.{Style.RESET_ALL}")
            return False
        else:
            return True

    def __create_person_entity(self, new_person_information : dict):
        name = new_person_information ["Nome"]
        cell_phone = new_person_information ["Telefone"]
        table_to = new_person_information ["Mesa"]

        self.new_person = Person(name, cell_phone, table_to)
        person_repository.register_person_queue(self.new_person)


    def __format_response(self):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y, %H:%M:%S")

        os.system("cls||clear")

        print(f"""{Fore.LIGHTRED_EX}Você entrou na fila de espera - {date_time}{Style.RESET_ALL}\n
Procure o(a) recepcionista quando chegar.\n
""")
        input(f"Pressione enter para {Fore.LIGHTRED_EX}Acompanhar{Style.RESET_ALL}")

        return self.__preview_position()
        
    
    def __preview_position(self):
        information_position = person_repository.preview_position(self.new_person)
        position_general = information_position["posição geral"]
        position_exception = information_position["posição mesa"]

        os.system("cls||clear")

        print(f"""Sua posição na Mesa para {self.new_person.table_to} pessoa(as):\n
              {Fore.LIGHTRED_EX}{position_exception}°{Style.RESET_ALL}\n
Sua posição na fila geral:\n 
              {Fore.LIGHTRED_EX}{position_general}°{Style.RESET_ALL}\n
{Fore.LIGHTRED_EX}{Style.BRIGHT}[1]-Sair da fila de espera{Style.RESET_ALL}
{Fore.LIGHTRED_EX}{Style.BRIGHT}[2]-Voltar{Style.RESET_ALL}\n""")
        
        decision = False

        while not decision:
            if keyboard.is_pressed("1"):
                person_repository.exit_queue_person(self.new_person)
                break
            elif keyboard.is_pressed("2"):
                break
            else:
                continue  