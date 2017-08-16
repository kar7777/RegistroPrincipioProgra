#Imports
from ClassLogic.StudentLogic import *
from ClassLogic.CourseLogic import *
from ClassLogic.CareerLogic import *
studentIdentificationCardList = []
#List of Student Identification Card
def ListOfStudentIdentificationCards():
    studentList = GetStudenList()
    for j in range(len(studentList)):
        studentIdentificationCardList.append(studentList[j].identificationCard) # Save only the identification card
        print("Nombre del Estudiante: ", studentList[j].name," **Cédula: ", studentList[j].identificationCard)
# This function assigns a Student to a career
def AddStudentToCareer():
    ShowCareerList()
    careerList = GetCareerList()
    enterCareerPosition = input("\nIngrese la Carrera que quiere Agregar al estudiante: ")
    if not enterCareerPosition.isdigit():#Validate that only numbers are entered
        print("Haz ingresado un dato que no es un número.")
        return #If you do not enter a number, return it
    for i in range(len(careerList)):
        if i == int(enterCareerPosition):
            while True:
                print("1...Asignar un Estudiante a una Carrera.\n"
                      "0...Salir.")
                optionsEntry = input("\nIngrese una Opcion: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        ListOfStudentIdentificationCards()
                        addIdentificationCard = input("\nIngrese número de Cédula del Estudiante a Asignar: ")
                        addIdentificationCard = addIdentificationCard.upper()#Switch to uppercase
                        for o in studentIdentificationCardList: # Search in the identification card list
                            if o in addIdentificationCard: # If the identification card entered matches some identification card from the list
                                for k in careerList[i].studentList:
                                    if k == addIdentificationCard:# Verify that the entered identification card is not assigned
                                        # If the identification card is the same do not enter it
                                        print("El Estudiante ya esta Matriculado en es Carrera.")
                                        break
                                else: #If it is not the same add it
                                    careerList[i].studentList.append(addIdentificationCard)
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
#This feature delete a Student from a career
def DeleteStudentToCareer():
    ShowCareerList()
    careerList = GetCareerList()
    courseList = GetCourseList()
    enterCareerPosition = input("\nIngrese el Estudiante que quiere Eliminar de la Carrera: ")
    if not enterCareerPosition.isdigit():  #Validate that only numbers are entered
        print("Haz ingresado un dato que no es un número.")
        return #If you do not enter a number, return it
    for i in range(len(careerList)): #Search in all Student
        if i == int(enterCareerPosition): # If the entered position matches
            ListOfStudentIdentificationCards()
            deleteidentificationCard = input("\nIngrese la Cédula del Estudiante que desea eliminar: ")
            deleteidentificationCard = deleteidentificationCard.upper()#Switch to uppercase
            # If the identification card entered is the same as the Student identification card it eliminates it
            if deleteidentificationCard in careerList[i].studentList:
                careerList[i].studentList.remove(deleteidentificationCard)
                for j in range(len(courseList)):
                    for l in range(len(courseList)):
                        if careerList[i].courseList[j] == courseList[l].courseCode:
                            if deleteidentificationCard in courseList[l].studentList:
                                courseList[l].studentList.remove(deleteidentificationCard)
            else:
                    print("No haz Pulsado una Opción Correcta o el Estudiante no ha sido Matriculado.")
    SetCourseList(courseList)
    SetCareerList(careerList)
#This function shows the options
def StudentToCarrerMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1...Asignar un Estudiante a una Carrera.\n"
          "\t2...Desasignar un Estudiante una Carrera.\n"
          "\t3...Visualizar las asignaciones de la Carrera.\n"
          "\t0...Volver al Menú Operativo.")
#This function is chosen the option
def StudentToCarrerMenuOptions():
    while True:
        StudentToCarrerMenu()
        optionsEntry = input("\nIngrese la opción a Escoger: ")
        if optionsEntry== "1":
            AddStudentToCareer()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "2":
            DeleteStudentToCareer()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "3":
            ShowAsignationToCareer()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "0":
            break
        else:
            input("\nNo has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")
StudentToCarrerMenuOptions()