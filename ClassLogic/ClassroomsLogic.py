#Imports
from ClassTypes.ClassRooms import *
from ClassLogic.CourseLogic import *
from pathlib import Path
import pickle
#This function is responsible for creating, and opening the file
def GetClassRoomsList():
    # Path: Displays the file path
    myClassRoomsFile = Path("..\Files\ClassRoomsFile.pickle")
    if myClassRoomsFile.is_file():#the file exists
        with open("..\Files\ClassRoomsFile.pickle", "rb") as classRoomsFile:
            classRoomsList = pickle._load(classRoomsFile)#Show File Information
        return classRoomsList
    return[]#If the file does not exist, an empty list is created
#This function is responsible for saving to the list
def SetClassRoomsList(classRoomsList):
    with open("..\Files\ClassRoomsFile.pickle", "wb") as classRoomsFile:
        pickle._dump(classRoomsList, classRoomsFile)#Save
#Function to add Campus
def AddClassRooms():
    classRoomsList = GetClassRoomsList()
    codeEntry = input("Ingrese el Código del Aula: ")
    codeEntry = codeEntry.upper()#Switch to uppercase
    allCodeToClassRooms = []
    # Sort a list based on parameters
    sorterClassRoomsList = sorted(classRoomsList, key=lambda classRooms: classRooms.classRoomsCode)
    # Validate if a code exists
    for code in sorterClassRoomsList:
       allCodeToClassRooms.append(code.classRoomsCode)
    for i in range(len(allCodeToClassRooms)):
        if allCodeToClassRooms[i] == codeEntry:
            print("La Aula ya Existe.")
            break
    else:#Create if it does not exist
        campusBelongsEntry = input("Ingrese el Campus en el que Pertenece: ")
        newClassRooms = Classrooms(codeEntry,campusBelongsEntry)
        classRoomsList = GetClassRoomsList()
        classRoomsList.append(newClassRooms)
        SetClassRoomsList(classRoomsList)
#Function to remove Classrooms
def DeleteClassRooms():
    ShowCareerList()
    courseList = GetCourseList()
    classRoomsList = GetClassRoomsList()
    enterClassRoomsPosition = input("\nIngrese la posición del Aula que quiera Eliminar: ")
    if not enterClassRoomsPosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return#If you do not enter a number, return it
    #To remove from assignments
    for course in courseList:
        if classRoomsList[int(enterClassRoomsPosition)].classRoomsCode in course.classRoomsList:
            course.classRoomsList.remove(classRoomsList[int(enterClassRoomsPosition)].classRoomsCode)
    if classRoomsList[int(enterClassRoomsPosition)] in classRoomsList:
        classRoomsList.remove(classRoomsList[int(enterClassRoomsPosition)])
    SetClassRoomsList(classRoomsList)
    SetCourseList(courseList)
#Shows the attributes of the Classrooms
def ShowCareerList():
    classRoomsList = GetClassRoomsList()
    classRoomsNumber = 0
    for classRooms in classRoomsList:
        classRoomsNumber = classRoomsNumber + 1
        print("Número de Aula: ", classRoomsNumber - 1, " **Código: ", classRooms.classRoomsCode,
              " **Recinto donde se ubica el Aula: ", classRooms.classroomsCampusBelongs)
#Function that modifies the Classrooms
def ModifyClassRooms():
    ShowCareerList()
    classRoomsList = GetClassRoomsList()
    enterClassRoomsPosition = input("\nIngrese el Aula que quiere Modificar: ")
    if not enterClassRoomsPosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return #If you do not enter a number, return it
    classRoomsExist = False#To validate if the campus exists
    for i in range(len(classRoomsList)):
        if i == int(enterClassRoomsPosition):
            classRoomsExist = True
            while True:
                print("\t1...Modificar Código del Aula.\n",
                      "\t2...Modificar Lugar donde se encuentra el Aula.\n",
                      "\t0...Salir.")
                optionsEntry = input("\nIngrese la Opción a Escoger: ")
                if optionsEntry != "0" :
                    if optionsEntry == "1":
                        classRoomsList[i].classRoomsCode = input("Ingrese un Nuevo Código: ")
                        classRoomsList[i].classRoomsCode = classRoomsList[i].classRoomsCode.upper()#Switch to uppercase
                    elif optionsEntry == "2":
                        classRoomsList[i].classroomsCampusBelongs = input("Ingrese un Nuevo Recinto del aula: ")
                    else:
                        input("\nNo has pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciónes.")
                elif optionsEntry == "0":
                    print("Saliendo...")
                    break
    if not classRoomsExist:
        print("El Aula NO Existe.")
    SetClassRoomsList(classRoomsList)
#This function shows the options
def ClassRoomsMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1...Agregar Aula.\n"
          "\t2...Eliminar Aula.\n"
          "\t3...Ver Aulas.\n"
          "\t4...Modificar Aulas.\n"
          "\t0...Volver al Menú Administrativo.")
#This function is chosen the option
def ClassRoomsMenuOptions():
    while True:
        ClassRoomsMenu()
        optionsEntry = input("\nIngrese la opción a Escoger: ")
        if optionsEntry== "1" :
            AddClassRooms()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "2" :
            DeleteClassRooms()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "3" :
            ShowCareerList()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "4":
            ModifyClassRooms()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "0" :
            break
        else:
            input("\nNo has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")
ClassRoomsMenuOptions()