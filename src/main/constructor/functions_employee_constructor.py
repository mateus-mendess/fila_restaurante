from src.views.functions_employee_view import functions_employee_view
from src.views.register_employee_view import register_employee_view
from src.views.preview_queue_view import preview_queue_view
from src.controllers.register_employee_controller import RegisterEmployeeController
from src.controllers.served_people_controller import ServedPeopleController
from src.controllers.preview_queue_controller import PreviewQueueController

def functions_employee_constructor():
    while True:
        command = functions_employee_view()


        match command:
                case 1:
                    register_information = register_employee_view()

                    register_employee_controller = RegisterEmployeeController()
                    register_employee_controller.register_employee(register_information)
                    continue
                case 2:
                    served_people_controller = ServedPeopleController()
                    served_people_controller.served()
                    continue
                case 3:
                    command_preview = preview_queue_view()

                    preview_queue_controller = PreviewQueueController()
                    preview_queue_controller.preview(command_preview)
                    continue
                case 8:
                    break
                case _:
                    break
