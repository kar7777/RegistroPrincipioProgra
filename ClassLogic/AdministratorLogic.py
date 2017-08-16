#Imports
import pickle
from pathlib import Path
from ClassTypes.Administrator import *
#This function is responsible for creating, and opening the file
def GetAdministratorLogin():
    #Path: Displays the file path
    myAdministratorLogin = Path("..\Files\AdministratorFile.pickle")
    if myAdministratorLogin.is_file():#If the file exists
        with open("..\Files\AdministratorFile.pickle", "rb") as administratorFile:#Show File Information
            administratorLogin = pickle._load(administratorFile)
        return administratorLogin
    return[] #If the file does not exist, an empty list is created
#
def SetAdministratorLogin(administratorLogin):
    with open("..\Files\AdministratorFile.pickle", "wb") as administratorFile:
        pickle._dump(administratorLogin, administratorFile)
#This function is responsible for saving and modifying the administrator data
def ChangePassword():
    administratorLogin = GetAdministratorLogin()
    administratorLogin = Admin("karlonso", "12345")
    changePasswordEntry = input("Ingrese la nueva contraseña:")
    administratorLogin.password = changePasswordEntry
    SetAdministratorLogin(administratorLogin)
    print("Tu Contraseña Ha siado Cambiada.")