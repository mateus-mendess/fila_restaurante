from src.models.repository.employee_repository import employee_repository
from colorama import Fore, Style

class LoginEmployeeController:
    def login(self, login_information):
         validate = self.__authentication(login_information)
         self.__format_response(validate)
         return validate

    def __authentication(self, login_information):
        user = login_information["usuario"]
        password = login_information["senha"]

        validate = employee_repository.authentication_employee(user, password)

        return validate
    
    def __format_response(self, validate):
        if not validate:
            print(f"{Fore.LIGHTRED_EX}\nUsuario ou senha incorreta.\n{Style.RESET_ALL}")
            input("Pressione enter para voltar...")
        else:
            pass

