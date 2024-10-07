from src.models.entities.person import Person
from collections import deque
from datetime import datetime

class PersonRepository:
    def __init__(self):
        self.queue_general = deque()

        self.queue_table_one = deque()
        self.queue_table_two = deque()
        self.queue_table_three = deque()
        self.queue_table_four = deque()
        self.queue_table_more = deque()

        self.queue_served = deque()


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

    def preview_position(self, person: Person):
        self.table_map = {
            "1": self.queue_table_one,
            "2": self.queue_table_two,
            "3": self.queue_table_three,
            "4": self.queue_table_four,
            "5+": self.queue_table_more
        }

        self.position_general = self.queue_general.index(person)
        self.position_exception = self.table_map[person.table_to].index(person)

        information_position = {
            "posição geral": self.position_general,
            "posição mesa": self.position_exception
        }

        return information_position
    
    def exit_queue_person(self, person: Person):
        for client in range(len(self.queue_general)):
            if self.queue_general[client] == person:
                del self.queue_general[client]

                if person.table_to in self.table_map:
                    if self.position_exception < len(self.table_map[person.table_to]):
                        del self.table_map[person.table_to][self.position_exception]

    def served_person(self):
        if self.queue_general:
            person_served_general = self.queue_general.popleft()
            person_served_exception = person_served_general.table_to
        else:
            return False

        new_queue = deque()

        while self.table_map[person_served_exception]:
            client = self.table_map[person_served_exception].popleft()
            if client != person_served_general:
                new_queue.append(client)

        self.table_map[person_served_exception] = new_queue

        self.queue_served.append(person_served_general)

        return person_served_general
    
    def person_served_next(self):
        if self.queue_general:
            for person in self.queue_general:
                return person
        else:
            return False

    def preview_queue_general(self, command):
        match command:
            case 1:
                if not self.queue_general:
                    return False

                dados = [[person.cell_phone, person.name, person.table_to] for person in self.queue_general]
                return dados
            case 2:
                if not self.queue_table_one:
                    return False

                dados = [[person.cell_phone, person.name, person.table_to] for person in self.queue_table_one]
                return dados
            case 3:
                if not self.queue_table_two:
                    return False

                dados = [[person.cell_phone, person.name, person.table_to] for person in self.queue_table_two]
                return dados
            case 4:
                if not self.queue_table_three:
                    return False

                dados = [[person.cell_phone, person.name, person.table_to] for person in self.queue_table_three]
                return dados
            case 5:
                if not self.queue_table_four:
                    return False

                dados = [[person.cell_phone, person.name, person.table_to] for person in self.queue_table_four]
                return dados
            case 6:
                if not self.queue_table_more:
                    return False

                dados = [[person.cell_phone, person.name, person.table_to] for person in self.queue_table_more]
                return dados
            case 7:
                dados = 7
                return dados

person_repository = PersonRepository() 

