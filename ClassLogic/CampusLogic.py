#Imports
from ClassTypes.Campus import *
from ClassLogic.CourseLogic import *
import pickle
from pathlib import Path
#This function is responsible for creating, and opening the file
def GetCampusList():
    #Path: Displays the file path
    myCampusFile = Path("..\Files\CampusFile.pickle")
    if myCampusFile.is_file():#the file exists
        with open("..\Files\CampusFile.pickle", "rb") as campusFile:
            campusList = pickle._load(campusFile)#Show File Information
        return campusList
    return [] #If the file does not exist, an empty list is created
#This function is responsible for saving to the list
def SetCampusList(campusList):
    with open("..\Files\CampusFile.pickle", "wb") as campusFile:
        pickle._dump(campusList, campusFile)#Save
#Function to add Campus
def AddCampus():
    campusList = GetCampusList()
    codeEntry = input("Ingrese el Código del Recinto: ")
    codeEntry = codeEntry.upper()#Switch to uppercase
    allCodeToCampus = []
    #Sort a list based on parameters
    sorterCampusList = sorted(campusList, key=lambda campus: campus.campusCode)
    #Validate if a code exists
    for code in sorterCampusList:
        allCodeToCampus.append(code.campusCode)
    for j in range(len(allCodeToCampus)):
        if allCodeToCampus[j] == codeEntry:
            print("El Recinto ya Existe.")
            break
    else:#Create if it does not exist
        nameEntry = input("Ingrese el Nombre del Recinto: ")
        addressEntry = input("Ingrese la Dirección del Recinto: ")
        newCampus = Campus(nameEntry,addressEntry,codeEntry)
        campusList = GetCampusList()
        campusList.append(newCampus)
        SetCampusList(campusList)
#Function to remove campus
def DeleteCampus():
    #Validar si el numero ingresado es mayor que el del indice
    campusList = GetCampusList()
    courseList = GetCourseList()
    ShowCampusList()
    enterCampusPosition = input("\nIngrese la posición del Recinto que quiera eliminar: ")
    if not enterCampusPosition.isdigit(): #Validate that only numbers are entered
        print("Haz ingresado un dato que no es un número.")
        return #If you do not enter a number, return it
    #To remove from assignments
    for course in courseList:
        if campusList[int(enterCampusPosition)].campusCode in course.campusList:
            course.campusList.remove(campusList[int(enterCampusPosition)].campusCode)
    if campusList[int(enterCampusPosition)] in campusList:
        campusList.remove(campusList[int(enterCampusPosition)])
    SetCampusList(campusList)
    SetCourseList(courseList)
#Shows the attributes of the campus
def ShowCampusList():
    campusNumber = 0
    campusList = GetCampusList()
    for campus in campusList:
        campusNumber = campusNumber + 1
        print("Número de Recinto: ",campusNumber - 1," **Nombre: ",campus.campusName," **Dirección: ",campus.campusAddress ,
              " **Código: ",campus.campusCode)
#Function that modifies the campus
def ModifyCampus():
    ShowCampusList()
    campusList = GetCampusList()
    enterCampusPosition = input("\nIngrese el numero del Recinto que quiera Modificar: ")
    if not enterCampusPosition.isdigit(): #Validate that only numbers are entered
        print("Haz ingresado un dato que no es un número.")
        return #If you do not enter a number, return it
    campusExist = False#To validate if the campus exists
    for i in range(len(campusList)):
        if i == int(enterCampusPosition):
            campusExist = True
            while True:
                print("\t1...Modificar Nombre del Recinto.\n",
                      "\t2...Modifciar Dirección del Recinto.\n",
                      "\t3...Modificar Código del Recinto.\n",
                      "\t0...Salir.")
                optionsEntry = input("\nIngrese la Opción a Escoger: ")
                #Options to modify
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        campusList[i].campusName = input("Ingrese nuevo Nombre: ")
                    elif optionsEntry == "2":
                        campusList[i].campusAddress = input("Ingrese la nueva Dirección: ")
                    elif optionsEntry == "3":
                        campusList[i].campusCode = input("Ingrese el nuevo Código: ")
                        campusList[i].campusCode = campusList[i].campusCode.upper()#Switch to uppe|rcase
                    else:
                        input("\nNo has pulsado ninguna opción correcta...\n"
                                  "Presione una tecla para volver a las Opciones.")
                elif optionsEntry == "0":
                    print("Saliendo...")
                    break
    if not campusExist:
        print("El Recinto NO Existe.")
    SetCampusList(campusList)
#Options to modify
def CampusMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1...Agregar Recinto.\n"
          "\t2...Eliminar Recinto.\n"
          "\t3...Ver Recintos.\n"
          "\t4...Modificar Recinto.\n"
          "\t0...Volver al Menú Administrativo.")
#This function is chosen the option
def CampusMenuOptions():
    while True:
        CampusMenu()
        optionsEntry = input("\nIngrese la Opción a Escoger: ")
        if optionsEntry == "1":
            AddCampus()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "2":
            DeleteCampus()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "3":
            ShowCampusList()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "4":
            ModifyCampus()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "0":
            break
        else:
            input("\nNo has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú.")
CampusMenuOptions()