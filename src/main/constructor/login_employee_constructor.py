from src.views.login_employee_view import login_employee_view
from src.controllers.login_employee_controller import LoginEmployeeController

def login_employee_constructor():
    login_information = login_employee_view()

    login_employee_controller = LoginEmployeeController()
    validate = login_employee_controller.login(login_information)

    return validate
    