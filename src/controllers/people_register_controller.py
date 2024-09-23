from src.models.repository.person_repository import person_repository
from src.models.entities.person import Person
from colorama import Fore, Style
import os

class PeopleRegisterController:

    def register(self, new_person_information: dict):
        try:
            if self.__check_name(new_person_information):
                self.__create_person_entity(new_person_information)
                response = self.__format_response()
                return response
            else:
                pass
        except Exception as exception:
            print(str(exception))

    def __check_name(self, new_person_information):
        name_person = new_person_information ["Nome"]
        
        if not name_person.replace(" ", "").isalpha():
            print(f"{Fore.LIGHTRED_EX}Nome incorreto.{Style.RESET_ALL}")
            return False
        try: int(new_person_information["Telefone"])
        except ValueError:
            print("Telefone Inválido.")
            return False
        try: int(new_person_information["Mesa"])
        except ValueError:
            print("Quantidade de mesa inválida.")
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
        os.system("cls||clear")
        print(f"""{Fore.LIGHTRED_EX}Você entrou na fila de espera!{Style.RESET_ALL}\n
Procure o(a) recepcionista quando chegar.\n
""")
        input(f"Pressione enter para {Fore.LIGHTRED_EX}Acompanhar{Style.RESET_ALL}")
        
        os.system("cls||clear")

        return person_repository.preview_format(self.new_person)
         
        


    