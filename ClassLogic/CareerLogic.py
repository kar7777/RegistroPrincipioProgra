#Imports
import pickle
from pathlib import Path
from ClassTypes.Career import Career
#This function is responsible for creating, and opening the file
def GetCareerList():
    # Path: Displays the file path
    myCareerFile = Path("..\Files\CareerFile.pickle")
    if myCareerFile.is_file():#the file exists
        with open("..\Files\CareerFile.pickle", "rb") as careerFile:
            careerList = pickle._load(careerFile)#Show File Information
        return careerList
    return[]#If the file does not exist, an empty list is created
#This function is responsible for saving to the list
def SetCareerList(careerList):
    with open("..\Files\CareerFile.pickle", "wb") as careerFile:
        pickle._dump(careerList, careerFile)#Save
#Function to add Campus
def AddCareer():
    careerList = GetCareerList()
    codeEntry = input("Ingrese el Código de la Carrera: ")
    codeEntry = codeEntry.upper()#Switch to uppercase
    allCodeToCareer = []
    # Sort a list based on parameters
    sorterCareerList = sorted(careerList, key=lambda career: career.code)
    # Validate if a code exists
    for codeCareer in sorterCareerList:
        allCodeToCareer.append(codeCareer.code)
    for i in range(len(allCodeToCareer)):
        if allCodeToCareer[i] == codeEntry:
            print("Esta Carrera ya Existe.")
            break
    else:#Create if it does not exist
        nameEntry = input("Ingrese el Nombre de la Carerra: ")
        newCareer = Career(nameEntry, codeEntry)
        careerList.append(newCareer)
        SetCareerList(careerList)
#Function to remove campus
def DeleteCareer():
    ShowCareerList()
    careerList = GetCareerList()
    enterCareerPosition = input("\nIngrese la posición de la Carrera que quiera Eliminar: ")
    if not enterCareerPosition.isdigit(): #Validate that only numbers are entered
        print("Haz ingresado un dato que no es un número.")
        return #If you do not enter a number, return it
    careerList.remove(careerList[int(enterCareerPosition)])
    SetCareerList(careerList)
#Shows the attributes of the campus
def ShowCareerList():
    careerNumber = 0
    careerList = GetCareerList()
    for career in careerList:
        careerNumber = careerNumber + 1
        print("Número de Carrera: ", careerNumber - 1," **Nombre: ",career.name," **Código: ",career.code)
#Function that modifies the career
def ModifyCareer():
    ShowCareerList()
    careerList = GetCareerList()
    enterCareerPosition = input("\nIngrese la Carrera que quiere Modificar: ")
    if not enterCareerPosition.isdigit():#Validate that only numbers are entered
        print("Haz ingresado un dato que no es un número.")
        return#If you do not enter a number, return it
    careerExist = False#To validate if the campus exists
    for i in range(len(careerList)):
        if i == int(enterCareerPosition):
            careerExist = True
            while True:
                print("\t1...Modificar Nombre de la Carrera.\n",
                      "\t2...Modificar Código de la Carrerra.\n",
                      "\t0...Salir.")
                optionsEntry = input("\nIngrese la Opción a Escoger: ")
                # Options to modify
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        careerList[i].name = input("Ingrese un nuevo Nombre: ")
                    elif optionsEntry == "2":
                        careerList[i].code = input("Ingrese un nuevo Código: ")
                        careerList[i].code = careerList[i].code.upper()#Switch to uppercase
                    else:
                        input("\nNo has pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciónes.")
                elif optionsEntry == "0":
                    print("Saliendo...")
                    break
    if not careerExist:
        print("La Carrera NO Existe.")
    SetCareerList(careerList)
#This function is used to show the assignments of the career
def ShowAsignationToCareer():
    careerList = GetCareerList()
    careerNumber = 0
    for career in careerList:
        careerNumber = careerNumber + 1
        print("Número de Carrera: ", careerNumber - 1, " **Nombre: ", career.name, " **Código: ", career.code,
              " **Lista de Cursos de la Carrera: ",career.courseList," \n\t**Lista de Docentes de la  Carrera: ",career.teacherList,
              " **Lista de Estudiantes de la Carrera: ",career.studentList)
#This function shows the options
def CareerMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1...Agregar Carrera.\n"
          "\t2...Eliminar Carrera.\n"
          "\t3...Ver Carrera.\n"
          "\t4...Modificar Carrera.\n"
          "\t0...Volver al Menú Administrativo.")
#This function is chosen the option
def CareerMenuOptions():
    while True:
        CareerMenu()
        optionsEntry = input("\nIngrese la opción a Escoger: ")
        if optionsEntry == "1":
            AddCareer()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "2":
            DeleteCareer()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "3":
            ShowCareerList()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "4":
            ModifyCareer()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "0":
            break
        else:
            input("\nNo has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")
CareerMenuOptions()