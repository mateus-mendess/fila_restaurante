from src.models.repository.person_repository import person_repository
from src.models.repository.employee_repository import employee_repository
from src.models.entities.employee import Employee
from colorama import Fore, Style


class RegisterEmployeeController:
    def register_employee(self, register_information):
        try:
            validate = self.__validate_register_employee(register_information)
            if validate:
                print(f"{Fore.LIGHTRED_EX}\nFuncionário Cadastrado.{Style.RESET_ALL}")
            else:
                print(f"{Fore.LIGHTRED_EX}\nNome de usuario já existe.{Style.RESET_ALL}")
        except Exception as exception:
            print(str(exception))

        input("\nPressione enter para voltar...")

    def __validate_register_employee(self, register_information):
        self.name = register_information["nome"]
        self.user = register_information["usuario"]
        self.password = register_information["senha"]

        if not self.name.replace(" ", "").isalpha():
            print(f"\n{Fore.LIGHTRED_EX}Nome incorreto.{Style.RESET_ALL}")
            return False
        elif employee_repository.validate_user_employee(self.user):
            if self.contains_uppercase(self.user):
                print(f"\n{Fore.LIGHTRED_EX}Por favor, utilize apenas letras minusculas, números e caracteres especiais{Style.RESET_ALL}")
                return False
            new_employee = Employee(self.name, self.user, self.password)
            employee_repository.register_employee(new_employee)
            return True
        return False

    def contains_uppercase(self, user):
        return any(char.isupper() for char in user)