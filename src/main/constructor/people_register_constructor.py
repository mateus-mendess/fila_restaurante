from src.views.people_register_view import register_people_view
from src.controllers.people_register_controller import PeopleRegisterController

def people_register_constructor():
    #view -> troca de informação com o usuario
    new_person_information = register_people_view()

    #controller -> minhas regras de negocio, verificações...
    people_register_controller = PeopleRegisterController()
    people_register_controller.register_people(new_person_information)

