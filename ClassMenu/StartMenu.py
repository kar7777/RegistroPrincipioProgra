#Imports
from ClassMenu.AdministrativeMenu import *
from ClassLogic.AdministratorLogic import *
#This function displays a message
def Menu():
    print("==================================\n"
          " Gestion de Elementons Principales\n"
          " Respecto a la Educación de la UTN\n"
          "==================================\n")
#The program is accessed
def DataManager():
    Menu()
    idEntry = input("Digite Usuario\n---> ")
    passwordEntry = input("Digite Contra\n---> ")
    administratorLogin = GetAdministratorLogin()
    if idEntry == administratorLogin.id and passwordEntry == administratorLogin.password:
        SetAdministratorLogin(administratorLogin)
        ChooseOption()
    else:
        print("Usuario o Contraseña Incorreta.")
DataManager()