#Imports
from ClassLogic.TeacherLogic import *
from ClassLogic.CourseLogic import *
teacherIdentificationCardList = []
#List of Teacher Identification Card
def ListOfTeacherIdentificationCard():
    teacherList = GetTeacherList()
    for j in range(len(teacherList)):
        teacherIdentificationCardList.append(teacherList[j].teacherIdentificationCard) # Save only the identification card
        print("Nombre del Docente: ", teacherList[j].teacherName, " **Cédula del Docente: ",teacherList[j].teacherIdentificationCard)
# This function assigns a Teacher to a career
def AddTeacherToCourses():
    ShowCourseList()
    courseList = GetCourseList()
    careerList = GetCareerList()
    enterCoursePosition = input("\nIngrese el Curso que quiere Asignarle un Docente: ")
    if not enterCoursePosition.isdigit():#Validate that only numbers are entered
        print("Haz ingresado un dato que no es un número.")
        return #If you do not enter a number, return it
    for i in range(len(courseList)):
        if i == int(enterCoursePosition):
            while True:
                print("1...Asignar un Docente a un Curso.\n"
                      "0...Salir.")
                optionsEntry = input("\nIngrese una Opcion: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        ListOfTeacherIdentificationCard()
                        addIdentificationCard = input("\nIngrese número de Cédula del Docente a Asignar: ")
                        addIdentificationCard = addIdentificationCard.upper() #Switch to uppercase
                        for o in teacherIdentificationCardList:  # Search in the identification card list
                            if o in addIdentificationCard: # If the identification card entered matches some identification card from the list
                                for k in courseList[i].teacherList:
                                    if k == addIdentificationCard: # Verify that the entered identification card is not assigned
                                        # If the identification card is the same do not enter it
                                        print("Este Docente ya está Registrado en este Curso.")
                                        break
                                else:  #If it is not the same add it
                                    #Validate if a course belongs to more than one career
                                    careerIndexes = []
                                    for q in range(len(careerList)):
                                        for careerCourse in careerList[q].courseList:#Find the list of courses for each career
                                            if careerCourse == courseList[i].courseCode:
                                                careerIndexes.append(q)
                                    if len(careerIndexes) == 0:
                                        print("Este curso no esta asignado a ninguna carrera, por favor asignarlo, antes de asignarle un Docente.")
                                        break
                                    elif len(careerIndexes) == 1:
                                        # validate not repeat students
                                        if not addIdentificationCard in careerList[careerIndexes[0]].teacherList:
                                            careerList[careerIndexes[0]].teacherList.append(addIdentificationCard)
                                    else:#If the course is assigned to more than one career choose where to assign the teacher
                                        print("A cual carrera quiere asignar el docente")
                                        for e in careerIndexes:
                                            print(e, careerList[i].name)
                                        careerseleted = int(input("digite la posicion de la carrera"))
                                        # validate not repeat teacher
                                        if not addIdentificationCard in careerList[careerseleted].teacherList:
                                            careerList[careerseleted].teacherList.append(addIdentificationCard)
                                        else:
                                            print("El estudiante ya esta matriculado en esta carrera")
                                    courseList[i].teacherList.append(addIdentificationCard)
                                    print(courseList[i].teacherList)
                                    SetCourseList(courseList)
                                    SetCareerList(careerList)
                                    break
                        else:
                            print("La Cédula del Docente no Existe.\n")
                    else:
                        input("\nNo has pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciones.")
                elif optionsEntry == "0":
                    print("Saliendo...")
                    break
#This feature delete a Teacher from a career
def DeleteTeacherLogicToCourses():
    ShowCourseList()
    courseList = GetCourseList()
    enterCoursePosition = input("\nIngrese el Curso que quiere Eliminarle un Docente: ")
    if not enterCoursePosition.isdigit():#Validate that only numbers are entered
        print("Haz ingresado un dato que no es un número.")
        return #If you do not enter a number, return it
    for i in range(len(courseList)):#Search in all Teacher
        if i == int(enterCoursePosition): # If the entered position matches
            ListOfTeacherIdentificationCard()
            deleteCode = input("Ingrese el codigo que desea eliminar")
            deleteCode = deleteCode.upper() #Switch to uppercase
            if deleteCode in courseList[i].teacherList:
                courseList[i].teacherList.remove(deleteCode)
            else:
                print("No haz Pulsado una Opción Correcta o No Exite el número de Cédula")
    SetCourseList(courseList)
#This function shows the options
def TeacherToCoursesMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1...Asignar un Docente a un Curso.\n"
          "\t2...Desasignar un Docente a un Curso.\n"
          "\t3...Visualizar las asignaciones del Cursos.\n"
          "\t0...Volver al Menú Operativo.")
#This function is chosen the option
def TeacherToCoursesMenuOptions():
    while True:
        TeacherToCoursesMenu()
        optionsEntry = input("\nIngrese la opción a Escoger: ")
        if optionsEntry== "1" :
            AddTeacherToCourses()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "2":
            DeleteTeacherLogicToCourses()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "3":
            ShowAsignationToCourses()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "0":
            break
        else:
            input("\nNo has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")
TeacherToCoursesMenuOptions()