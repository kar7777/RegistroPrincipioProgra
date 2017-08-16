#Imports
from ClassLogic.CareerLogic import *
from ClassTypes.Course import *
from pathlib import Path
import pickle
##This function is responsible for creating, and opening the file
def GetCourseList():
    # Path: Displays the file path
    myCourseFile = Path("..\Files\CourseFile.pickle")
    if myCourseFile.is_file():#the file exists
        with open("..\Files\CourseFile.pickle", "rb") as courseFile:
            courseList = pickle._load(courseFile)#Show File Information
        return courseList
    return []#If the file does not exist, an empty list is created
#This function is responsible for saving to the list
def SetCourseList(courseList):
    with open("..\Files\CourseFile.pickle", "wb") as courseFile:
        pickle._dump(courseList,courseFile)#Save
#Function to add Campus
def AddCourse():
    courseList = GetCourseList()
    codeEntry = input("Ingrese el Código del Curso: ")
    codeEntry = codeEntry.upper ()#Switch to uppercase
    allCodeToCourse = []
    # Sort a list based on parameters
    sorterCourseList = sorted(courseList, key=lambda course: course.courseCode)
    # Validate if a code exists
    for code in sorterCourseList:
        allCodeToCourse.append(code.courseCode)
    for i in range(len(allCodeToCourse)):
        if allCodeToCourse[i] == codeEntry:
            print("El Curso ya Existe.")
            break
    else:#Create if it does not exist
        nameEntry = input("Ingrese el Nombre del Curso: ")
        newCourse = Course(nameEntry,codeEntry)
        courseList.append(newCourse)
        SetCourseList(courseList)
#Function to remove campus
def DeleteCourse():
    # Validar si el numero ingresado es mayor que el del indice
    ShowCourseList()
    courseList = GetCourseList()
    careerList = GetCareerList()
    enterCoursePosition = input("\nIngrese la posición del Curso que quiera Eliminar: ")
    if not enterCoursePosition.isdigit():#Validate that only numbers are entered
        print("Haz ingresado un dato que no es un número.")
        return #If you do not enter a number, return it
    # To remove from assignments
    for career in careerList:
        if courseList[int(enterCoursePosition)].courseCode in career.courseList:
            career.courseList.remove(courseList[int(enterCoursePosition)].courseCode)
    if courseList[int(enterCoursePosition)] in courseList:
        courseList.remove(courseList[int(enterCoursePosition)])
    SetCourseList(courseList)
    SetCareerList(careerList)
#Shows the attributes of the course
def ShowCourseList():
    courseNumber = 0
    courseList = GetCourseList()
    for course in courseList:
        courseNumber = courseNumber + 1
        print("Número de Curso: ",courseNumber - 1," **Nombre: ",course.courseName, " **Código: ",course.courseCode)
#Function that modifies the course
def ModifyCourse():
    ShowCourseList()
    enterCoursePosition = input("\nIngrese el numero del Curso que quiera Modificar: ")
    if not enterCoursePosition.isdigit(): #Validate that only numbers are entered
        print("Haz ingresado un dato que no es un número.")
        return #If you do not enter a number, return it
    courseList = GetCourseList()
    courseExist = False#To validate if the campus exists
    for i in range(len(courseList)):
        if i == int(enterCoursePosition):
            courseExist = True
            while True:
                print("\t1...Modificar Nombre del Curso.\n",
                      "\t2...Modificar Código del Curso.\n",
                      "\t0...Salir.")
                optionsEntry = input("\nIngrese la Opción a Escoger: ")
                # Options to modify
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        courseList[i].courseName = input("Ingrese nuevo Nombre: ")
                    elif optionsEntry == "2":
                        courseList[i].courseCode = input("Ingrese el nuevo Código: ")
                        courseList[i].courseCode = courseList[i].courseCode.upper()#Switch to uppercase
                    else:
                        input("\nNo has pulsado ninguna opción correcta...\n"
                              "Presione una tecla para volver a las Opciones.")
                elif optionsEntry == "0":
                    print("Saliendo...")
                    break
    if not courseExist:
        print("El Curso NO Existe.")
    SetCourseList(courseList)
#This function is used to show the assignments of the course
def ShowAsignationToCourses():
    courseList = GetCourseList()
    courseNumber = 0
    for course in courseList:
        courseNumber = courseNumber + 1
        print("Número de Curso: ", courseNumber - 1, " **Nombre: ", course.courseName, " **Código: ", course.courseCode,
              " **Lista de Estudiantes: ", course.studentList, " \n\t**Lista de Profesores: ", course.teacherList,
              " **Recinto donde Pertenece: ", course.campusList, " **Aulas donde se Imparten Clases: ",
              course.classRoomsList," **Horario del Curso: ", course.classScheduleList)
#This function shows the options
def CourseMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1...Agregar Curso.\n"
          "\t2...Eliminar Curso.\n"
          "\t3...Ver Cursos.\n"
          "\t4...Modificar Cursos.\n"
          "\t0...Volver al Menú Administrativo.")
#This function is chosen the option
def CourseMenuOptions():
    while True:
        CourseMenu()
        optionsEntry = input("\nIngrese la Opción a Escoger: ")
        if optionsEntry == "1":
            AddCourse()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "2":
            DeleteCourse()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "3":
            ShowCourseList()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "4":
            ModifyCourse()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "0":
            break
        else:
            input("\nNo has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú.")
CourseMenuOptions()