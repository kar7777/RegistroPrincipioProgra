#imports
from ClassLogic.TeacherLogic import *
from ClassLogic.CareerLogic import *
teacherIdentificationCardList = []
#List of Teacher Identification Card
def ListOfTeacherIdentificationCards():
    teacherList = GetTeacherList()
    for j in range(len(teacherList)):
        teacherIdentificationCardList.append(teacherList[j].teacherIdentificationCard) # Save only the identification card
        print("Nombre del Docente: ", teacherList[j].teacherName, " **Cédula del Docente: ",teacherList[j].teacherIdentificationCard)
# This function assigns a Teacher to a career
def AddTeacherToCareer():
    ShowCareerList()
    careerList = GetCareerList()
    enterCareerPosition = input("\nIngrese la Carrera que quiere Agregar Docentes: ")
    if not enterCareerPosition.isdigit(): #Validate that only numbers are entered
        print("Haz ingresado un dato que no es un número.")
        return #If you do not enter a number, return it
    for i in range(len(careerList)):
        if i == int(enterCareerPosition):
            while True:
                print("1...Asignar un Docente a una Carrera.\n"
                      "0...Salir.")
                optionsEntry = input("\nIngrese una Opcion: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        ListOfTeacherIdentificationCards()
                        addIdentificationCard = input("\nIngrese número de Cédula del Docente a Asignar: ")
                        addIdentificationCard = addIdentificationCard.upper() #Switch to uppercase
                        for o in teacherIdentificationCardList: # Search in the identification card list
                            if o in addIdentificationCard: # If the identification card entered matches some identification card from the list
                                for k in careerList[i].teacherList:
                                    if k == addIdentificationCard:# Verify that the entered identification card is not assigned
                                        # If the identification card is the same do not enter it
                                        print("Este Docente ya está Registrado en esta Carrera.")
                                        break
                                else: #If it is not the same add it
                                    careerList[i].teacherList.append(addIdentificationCard)
                                    print("Asignación Correcta.\n")
                                    SetCareerList(careerList)
                                    break
                        else:
                            print("La Cédula ingresada no Existe.\n")
                    else:
                        input("\nNo haz pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciones.")
                elif optionsEntry == "0":
                    print("Saliendo...")
                    break
#This feature delete a Teacher from a career
def DeleteTeacherToCareer():
    ShowCareerList()
    careerList = GetCareerList()
    courseList = GetCourseList()
    enterCareerPosition = input("\nIngrese la Carrera que quiere Eliminar Docentes: ")
    if not enterCareerPosition.isdigit():  #Validate that only numbers are entered
        print("Haz ingresado un dato que no es un número.")
        return #If you do not enter a number, return it
    for i in range(len(careerList)): #Search in all Teacher
        if i == int(enterCareerPosition): # If the entered position matches
            ListOfTeacherIdentificationCards()
            deleteCode = input("Ingrese la Cédula del Docente que desea eliminar: ")
            if deleteCode in careerList[i].teacherList:
                careerList[i].teacherList.remove(deleteCode)
                for j in range(len(careerList[i].courseList)):
                    for l in range(len(courseList)):
                        if careerList[i].courseList[j] == courseList[l].courseCode:
                            if deleteCode in courseList[l].teacherList:
                                courseList[l].teacherList.remove(deleteCode)
            else:
                print("No haz Pulsado una Opción Correcta o No Existe el número de Cédula.")

    SetCourseList(courseList)
    SetCareerList(careerList)
#This function shows the options
def TeacherToCareerMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1...Asignar un Docente a una Carrera.\n"
          "\t2...Desasignar un Docente a una Carrera.\n"
          "\t3...Visualizar las asignaciones de la Carrera.\n"
          "\t0...Volver al Menú Operativo.")
#This function is chosen the option
def TeacherToCareerMenuOptions():
    while True:
        TeacherToCareerMenu()
        optionsEntry = input("Ingrese la opción a Escoger: ")
        if optionsEntry== "1":
            AddTeacherToCareer()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "2":
            DeleteTeacherToCareer()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "3":
            ShowAsignationToCareer()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "0":
            break
        else:
            input("\nNo has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")
TeacherToCareerMenuOptions()