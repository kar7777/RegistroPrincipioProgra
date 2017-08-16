#imports
from ClassLogic.ClassroomsLogic import *
from ClassLogic.CourseLogic import *
#List of classRooms codes
codeList = []
#Shows the list of registered classRooms
def ListOfClassRoomsCodes():
    classRoomsList = GetClassRoomsList()
    for j in range(len(classRoomsList)):
        codeList.append(classRoomsList[j].classRoomsCode) # Save only the codes
        print("Código de Aula: ", classRoomsList[j].classRoomsCode, " **Recinto donde Pertenezca: ",
              classRoomsList[j].classroomsCampusBelongs)
# This function assigns a classRooms to a course
def AddClassRoomsToCourses():
    courseList = GetCourseList()
    ShowCourseList()
    enterCoursePosition = input("\nIngrese el Curso que quiere Asignarle un Aula: ")
    if not enterCoursePosition.isdigit(): #Validate that only numbers are entered
        print("Haz ingresado un dato que no es un número.")
        return #If you do not enter a number, return it
    for i in range(len(courseList)):
        if i == int(enterCoursePosition):
            while True:
                print("1...Asignar un Aula a un Curso.\n"
                      "0...Salir.")
                optionsEntry = input("\nIngrese una Opción: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        ListOfClassRoomsCodes()
                        addCode = input("\nIngrese Código del Aula a Asignar: ")
                        addCode = addCode.upper()#Switch to uppercase
                        for o in codeList: # Search in the code list
                            if o in addCode: # If the code entered matches some code from the list
                                for k in courseList[i].classRoomsList:
                                    if k == addCode:# Verify that the entered code is not assigned
                                        # If the code is the same do not enter it
                                        print("El Aula ya se Asignó a este Curso.")
                                        break
                                else:#If it is not the same add it
                                    courseList[i].classRoomsList.append(addCode)
                                    print("Asignación Correcta.\n")
                                    SetCourseList(courseList)
                                    break
                        else:
                            print("El Código del Aula no Existe.\n")
                    else:
                        input("\nNo has pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciónes.")
                elif optionsEntry == "0":
                    print("Saliendo...")
                    break
#This feature delete a classRooms from a course
def DeletClassRoomsToCourses():
    ShowCourseList()
    enterCoursePosition = input("\nIngrese el Curso que quiere Eliminarle Aulas: ")
    if not enterCoursePosition.isdigit():#Validate that only numbers are entered
        print("Haz ingresado un dato que no es un número.")
        return #If you do not enter a number, return it
    courseList = GetCourseList()
    for i in range(len(courseList)): #Search in all classRooms
        if i == int(enterCoursePosition):  # If the entered position matches
            ListOfClassRoomsCodes()
            deleteCode = input("\nIngrese el código del Aula que desea Eliminar: ")
            deleteCode = deleteCode.upper() #Switch to uppercase
            # If the code entered is the same as the classRooms code it eliminates it
            if deleteCode in courseList[i].classRoomsList:
                courseList[i].classRoomsList.remove(deleteCode)
                print("Desasignación Correcta.\n")
        else:
            print("No haz Pulsado una Opción Correcta o el Aula no ha sido Asignado.")
    SetCourseList(courseList)
#This function shows the options
def ClassRoomsToCoursesMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1...Asignar un Aula a un Curso.\n"
          "\t2...Desasignar un Aula a un Curso.\n"
          "\t3...Visualizar las asignaciones del Curso.\n"
          "\t0...Volver al Menú Operativo.")
#This function is chosen the option
def ClassRoomsToCoursesMenuOptions():
    while True:
        ClassRoomsToCoursesMenu()
        optionsEntry = input("\nIngrese la opción a Escoger: ")
        if optionsEntry == "1":
            AddClassRoomsToCourses()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "2":
            DeletClassRoomsToCourses()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "3":
            ShowAsignationToCourses()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "0":
            break
        else:
            input("\nNo has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")
ClassRoomsToCoursesMenuOptions()