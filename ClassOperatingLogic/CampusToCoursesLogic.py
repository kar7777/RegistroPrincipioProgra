#Imports
from ClassLogic.CampusLogic import *
from ClassLogic.CourseLogic import *
#List of campus codes
codeList = []
#Shows the list of registered campuses
def ListOfCampusCodes():
    campusList = GetCampusList()
    for j in range(len(campusList)):
        codeList.append(campusList[j].campusCode) # Save only the codes
        print("Nombre del Recinto: ", campusList[j].campusName, " **Código del Recinto: ", campusList[j].campusCode)
# This function assigns a campus to a course
def AddCampusToCourses():
    courseList = GetCourseList()
    ShowCourseList()
    enterCoursePosition = input("\nIngrese el Curso que quiere Agregarle Recintos: ")
    if not enterCoursePosition.isdigit():#Validate that only numbers are entered
        print("Haz ingresado un dato que no es un número.")
        return #If you do not enter a number, return it
    for i in range(len(courseList)):
        if i == int(enterCoursePosition):
            while True:
                print("1...Asignar un Recinto a un Curso.\n"
                      "0...Salir.")
                optionsEntry = input("\nIngrese una Opción: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        ListOfCampusCodes()
                        addCode = input("\nIngrese Código del Recinto a Asignar: ")
                        addCode = addCode.upper()#Switch to uppercase
                        for o in codeList:# Search in the code list
                            if o in addCode:# If the code entered matches some code from the list
                                for k in courseList[i].campusList:
                                    if k == addCode: # Verify that the entered code is not assigned
                                        # If the code is the same do not enter it
                                        print("El Recinto ya se Asignó a este curso.")
                                        break
                                else: #If it is not the same add it
                                    courseList[i].campusList.append(addCode)
                                    print("Asignación Correcta.\n")
                                    SetCourseList(courseList)
                                    break
                        else:
                            print("El Código del Recinto no Existe.\n")
                    else:
                        input("\nNo has pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciones.")
                elif optionsEntry == "0":
                    print("Saliendo...")
                    break
#This feature delete a campus from a course
def DeleteCampusToCourse():
    ShowCourseList()
    enterCoursePosition = input("\nIngrese el Curso que quiere Eliminarle Recintos: ")
    if not enterCoursePosition.isdigit(): #Validate that only numbers are entered
        print("Haz ingresado un dato que no es un número.")
        return #If you do not enter a number, return it
    courseList = GetCourseList()
    for i in range(len(courseList)): #Search in all courses
        if i == int(enterCoursePosition): # If the entered position matches
            ListOfCampusCodes()
            deleteCode = input("\nIngrese el código del Recinto que desea Eliminar: ")
            deleteCode = deleteCode.upper() #Switch to uppercase
            # If the code entered is the same as the campus code it eliminates it
            if deleteCode in courseList[i].campusList:
                courseList[i].campusList.remove(deleteCode)
                print("Desasignación Correcta.\n")
        else:
            print("No haz Pulsado una Opción Correcta o el Recinto no ha sido Asignado.")
    SetCourseList(courseList)
#This function shows the options
def CampusToCourseMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1...Asignar un Recinto a un Curso.\n"
          "\t2...Desasignar un Recinto a un Curso.\n"
          "\t3...Visualizar las asignaciones del Curso.\n"
          "\t0...Volver al Menú Operativo.")
#This function is chosen the option
def CampusToCourseMenuOptions():
    while True:
        CampusToCourseMenu()
        optionsEntry = input("\nIngrese la opción a Escoger: ")
        if optionsEntry== "1":
            AddCampusToCourses()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "2":
            DeleteCampusToCourse()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "3":
            ShowAsignationToCourses()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "0":
            break
        else:
            input("\nNo has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")
CampusToCourseMenuOptions()