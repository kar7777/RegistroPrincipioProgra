#Imports
from ClassLogic.CourseLogic import *
from ClassLogic.CareerLogic import *
#List of courses codes
codeList = []
#Shows the list of registered courses
def ListOfCoursesCodes():
    courseList = GetCourseList()
    for j in range(len(courseList)):
        codeList.append(courseList[j].courseCode) #Save only the codes
        print("Nombre del Curso: ", courseList[j].courseName, " **Código del Curso: ", courseList[j].courseCode)
# This function assigns a courses to a career
def AddCourseToCareer():
    careerList = GetCareerList()
    ShowCareerList()
    enterCareerPosition = input("\nIngrese la Carrera que quiere Agregar Cursos: ")
    if not enterCareerPosition.isdigit():#Validate that only numbers are entered
        print("Haz ingresado un dato que no es un número.")
        return#If you do not enter a number, return it
    for i in range(len(careerList)):
        if i == int(enterCareerPosition):
            while True:
                print("1...Asignar un Curso a una Carrera.\n"
                      "0...Salir.")
                optionsEntry = input("\nIngrese una Opción: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        ListOfCoursesCodes()
                        addCode = input("\nIngrese el código del Curso a Asignar: ")
                        addCode = addCode.upper()#Switch to uppercase
                        for o in codeList:# Search in the code list
                            if o in addCode:# If the code entered matches some code from the list
                                for k in careerList[i].courseList:
                                    if k == addCode:# Verify that the entered code is not assigned
                                        # If the code is the same do not enter it
                                        ############## Borrar
                                        print("El Curso ya está en esta Carrera.")
                                        break
                                else:#If it is not the same add it
                                    careerList[i].courseList.append(addCode)
                                    print("Asignación Correcta.\n")
                                    SetCareerList(careerList)
                                    break
                        else:
                            print("El Código del Curso no Existe.\n")
                    else:
                        input("\nNo has pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciones.")
                elif optionsEntry == "0":
                    print("Saliendo...")
                    break
#This feature delete a courses from a career
def DeleteCourseToCareer():
    ShowCareerList()
    careerList = GetCareerList()
    enterCareerPosition = input("\nIngrese la Carrera que quiere Eliminar Cursos: ")
    if not enterCareerPosition.isdigit():#Validate that only numbers are entered
        print("Haz ingresado un dato que no es un número.")
        return#If you do not enter a number, return it
    for i in range(len(careerList)):#Search in all career
        if i == int(enterCareerPosition):# If the entered position matches
            ListOfCoursesCodes()
            deleteCode = input("\nIngrese el código del Curso que desea Eliminar: ")
            deleteCode = deleteCode.upper()#Switch to uppercase
            # If the code entered is the same as the course code it eliminates it
            if deleteCode in  careerList[i].courseList:
                careerList[i].courseList.remove(deleteCode)
                print("Desasignación Correcta.\n")
        else:
            print("No haz Pulsado una Opción Correcta o el Curso no ha sido Asignado.")
    SetCareerList(careerList)
#This function shows the options
def CourseToCarrerMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1...Asignar un Curso a una Carrera.\n"
          "\t2...Desasignar un Cursos a una Carrera.\n"
          "\t3...Visualizar las asignaciones de la Carrera.\n"
          "\t0...Volver al Menú Operativo.")
#This function is chosen the option
def CourseToCarrerMenuOptions():
    while True:
        CourseToCarrerMenu()
        optionsEntry = input("\nIngrese la opción a Escoger: ")
        if optionsEntry == "1":
            AddCourseToCareer()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "2":
            DeleteCourseToCareer()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "3":
            ShowAsignationToCareer()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "0":
            break
        else:
            input("\nNo has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")
CourseToCarrerMenuOptions()