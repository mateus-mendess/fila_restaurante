from src.models.entities.person import Person
from collections import deque
from colorama import Fore, Style

class PersonRepository:
    def __init__(self):
        self.queue_general = deque()
        self.queue_table_one = deque()
        self.queue_table_two = deque()
        self.queue_table_three = deque()
        self.queue_table_four = deque()
        self.queue_table_more = deque()

    def register_person_queue(self, person: Person):
        self.queue_general.append(person)

        table_queues = {
            "1": self.queue_table_one,
            "2": self.queue_table_two,
            "3": self.queue_table_three,
            "4": self.queue_table_four,
            "5+": self.queue_table_more
        }

        if person.table_to in table_queues:
            table_queues[person.table_to].append(person)
        else:
            self.queue_table_more.append(person)

    def preview_format(self, person: Person):
        table_map = {
            "1": self.queue_table_one,
            "2": self.queue_table_two,
            "3": self.queue_table_three,
            "4": self.queue_table_four,
            "5+": self.queue_table_more
        }

        position_general = self.queue_general.index(person) + 1
        position_exception = table_map[person.table_to].index(person) + 1

        print(f"""Sua posição na Mesa para {person.table_to} pessoa(as):\n
              {Fore.LIGHTRED_EX}{position_exception}°{Style.RESET_ALL}\n
Sua posição na fila geral:\n
              
              {Fore.LIGHTRED_EX}{position_general}°{Style.RESET_ALL}
""")
        return input(f"Obrigado, Por escolher a {Fore.LIGHTRED_EX}Galeto Sat's{Style.RESET_ALL}")


person_repository = PersonRepository() 

