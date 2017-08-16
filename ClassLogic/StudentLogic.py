#Imports
from ClassTypes.Student import *
from ClassLogic.CourseLogic import *
from ClassLogic.CareerLogic import *
import pickle
from pathlib import Path
#This function is responsible for creating, and opening the file
def GetStudenList():
    # Path: Displays the file path
    myStudentFile = Path("..\Files\StudentFile.pickle")
    if myStudentFile.is_file():#the file exists
        with open("..\Files\StudentFile.pickle", "rb") as studentFile:
            studentList = pickle._load(studentFile)#Show File Information
        return studentList
    return []#If the file does not exist, an empty list is created
#This function is responsible for saving to the list
def SetStudentList(studentList):
    with open("..\Files\StudentFile.pickle","wb") as studentFile:
        pickle._dump(studentList, studentFile)#Save
# Function to add Campus
def AddStudent():
    studentList = GetStudenList()
    identificationCardEntry = input("Ingrese el número de Cédula del Estudiante: ")
    domainStudent = '@est.utn.ac.cr'
    allIdToStudent = []
    # Sort a list based on parameters
    sorterStudentList = sorted(studentList, key=lambda student: student.identificationCard)
    # Validate if a code exists
    for idStudent in sorterStudentList:
        allIdToStudent.append(idStudent.identificationCard)
    for j in range(len(allIdToStudent)):
        if allIdToStudent[j] == identificationCardEntry:
            print("El Estudiante ya existe.")
            break
    else: #Create if it does not exist
        nameEntry = input("Ingrese el Nombre del Estudiante: ")
        lastNameEntry = input("Ingrese el Apellido del Estudiante: ")
        addressEntry = input("Ingrese la Dirección donde vive el Estudiante: ")
        phoneEntry = input("Ingrese el Número de Telefono del Estudiante: ")
        while True:
            emailEntry = input("Ingrese solo el nombre del Correo del Estudiante: ")
            if "@" in emailEntry:
                print("Error al ingresar el correo, ingrese solo el nombre sin el @...")
            else:
                emailEntry = emailEntry+domainStudent
                break
        newStudent = Student(nameEntry, lastNameEntry, identificationCardEntry, addressEntry, phoneEntry, emailEntry)
        studentList.append(newStudent)
        SetStudentList(studentList)
#Function to remove campus
def DeleteStudent():
    studentList = GetStudenList()
    careerList = GetCareerList()
    courseList = GetCourseList()
    ShowStudentList()
    enterStudentPosition = input("\nIngrese el numero del estudiante que quiera eliminar: ")
    if not enterStudentPosition.isdigit(): #Validate that only numbers are entered
        print("Haz ingresado un dato que no es un número.")
        return#If you do not enter a number, return it
    #To remove from assignments
    for career in careerList:
        if studentList[int(enterStudentPosition)].identificationCard in career.studentList:
            career.studentList.remove(studentList[int(enterStudentPosition)].identificationCard)
    for course in courseList:
        if studentList[int(enterStudentPosition)].identificationCard in course.studentList:
            course.studentList.remove(studentList[int(enterStudentPosition)].identificationCard)
    if studentList[int(enterStudentPosition)] in studentList:
        studentList.remove(studentList[int(enterStudentPosition)])
    SetStudentList(studentList)
    SetCareerList(careerList)
    SetCourseList(courseList)
# Shows the attributes of the campus
def ShowStudentList():
    #Preguntar si se imprimen las asignaciones
    studentNumber = 0
    studentList = GetStudenList()
    for student in studentList:
        studentNumber = studentNumber + 1
        print("Número del Estudiante: ",studentNumber - 1," **Nombre: ",student.name," **Apellido: ",student.lastName," **Cédula: ",
              student.identificationCard," **Número Telefonico: ",student.phone," **Dirección de Residencia: ",student.address,
              " **Correo Eléctronico ",student.email)
#Function that modifies the student
def ModifyStudent():
    ShowStudentList()
    studentList = GetStudenList()
    studentExist = False #To validate if the campus exists
    enterStudentPosition = input("\nIngrese el numero del estudiante que quiera Modificar: ")
    if not enterStudentPosition.isdigit(): #Validate that only numbers are entered
        print("Haz ingresado un dato que no es un número.")
        return #If you do not enter a number, return it
    for i in range(len(studentList)):
        if i == int(enterStudentPosition):
            studentExist = True
            while True:
                print("\t1...Modificar Nombre del Estudiante.\n",
                      "\t2...Modifciar Apellido del Estudiante.\n",
                      "\t3...Modificar el número de Cédula del Estudiante.\n",
                      "\t4...Modificar Residencia del Estudiante.\n",
                      "\t5...Modificar el número  de Telefono del Estudiante.\n",
                      "\t6...Modificar Correo del Estudiante.\n",
                      "\t0...Salir.")
                optionsEntry = input("\nIngrese la Opción a Escoger: ")
                # Options to modify
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        studentList[i].name = input("Ingrese nuevo Nombre: ")
                    elif optionsEntry == "2":
                        studentList[i].lastName = input("Ingrese nuevo Apellido: ")
                    elif optionsEntry == "3":
                        studentList[i].identificationCard = input("Ingrese nuevo número de Cédula: ")
                    elif optionsEntry == "4":
                        studentList[i].address = input("Ingrese nueva Dirección: ")
                    elif optionsEntry == "5":
                        studentList[i].phone = input("Ingrese nuevo numero telefonico: ")
                    elif optionsEntry == "6":
                        studentList[i].email = input("Ingrese nuevo Email: ")
                    else:
                        input("\nNo has pulsado ninguna opción correcta...\n"
                              "Presione una tecla para volver a las Opciones.")
                elif optionsEntry == "0":
                    print("Saliendo...")
                    break
    if not studentExist:
        print("El Estudiante NO Existe.")
    SetStudentList(studentList)
# Options to modify
def StudentMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1...Agregar Estudiante.\n"
          "\t2...Eliminar Estudiante.\n"
          "\t3...Ver Lista Estudianten.\n"
          "\t4...Modificar Estudiante.\n"
          "\t0...Volver al Menú Administrativo.")
#This function is chosen the option
def StudentMenuOptions():
    while True:
        StudentMenu()
        optionsEntry = input("\nIngrese la Opción a Escoger: ")
        if optionsEntry == "1":
            AddStudent()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "2":
            DeleteStudent()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "3":
            ShowStudentList()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "4":
            ModifyStudent()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "0":
            break
        else:
            input("\nNo has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú.")
StudentMenuOptions()