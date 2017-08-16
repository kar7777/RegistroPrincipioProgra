#Imports
from ClassLogic.ClassScheduleLogic import *
from ClassLogic.CourseLogic import *
#List of class schedule types
typeList = []
#Show the list of registered class schedules
def ListOfClassSchedulesTypes():
    classScheduleList = GetClassScheduleList()
    for j in range(len(classScheduleList)):
        typeList.append(classScheduleList[j].scheduleType)# Save only the types
        print("Tipo de Horario del Curso: ", classScheduleList[j].scheduleType,
              " **Hora de Inicio: ", classScheduleList[j].startOfSchedule,
              " **Hora de Salida: ", classScheduleList[j].endOfSchedule)
# This function assigns a class schudeles to a course
def AddClassScheduleToCourses():
    courseList = GetCourseList()
    ShowCourseList()
    enterCoursePosition = input("\nIngrese el Curso que quiere Agregarle un Horario: ")
    if not enterCoursePosition.isdigit():#Validate that only numbers are entered
        print("Haz ingresado un dato que no es un número.")
        return#If you do not enter a number, return it
    for i in range(len(courseList)):
        if i == int(enterCoursePosition):
            while True:
                print("1...Asignar un Horario a un Curso.\n"
                      "0...Salir.")
                optionsEntry = input("\nIngrese una Opcion: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        ListOfClassSchedulesTypes()
                        addType = input("\nIngrese el Tipo del Horario a Asignar: ")
                        addType = addType.upper()#Switch to uppercase
                        for o in typeList:# Search in the types list
                            if o in addType:# If the types entered matches some code from the list
                                for k in courseList[i].classScheduleList:
                                    if k == addType:# Verify that the entered type is not assigned
                                        # If the type is the same do not enter it
                                        print("El Horario ya se encuentra en este Curso.")
                                        break
                                else:#If it is not the same add it
                                    courseList[i].classScheduleList.append(addType)
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
#This feature delete a class schudele from a course
def DeleteClassScheduleToCourse():
    ShowCourseList()
    enterCoursePosition = input("\nIngrese el Curso que quiere Eliminarle un Horario: ")
    if not enterCoursePosition.isdigit():#Validate that only numbers are entered
        print("Haz ingresado un dato que no es un número.")
        return#If you do not enter a number, return it
    courseList = GetCourseList()
    for i in range(len(courseList)): #Search in all courses
        if i == int(enterCoursePosition):# If the entered position matches
            ListOfClassSchedulesTypes()
            deleteType = input("\nIngrese el Tipo del Horario que desea Eliminar: ")
            deleteType = deleteType.upper()#Switch to uppercase
            # If the type entered is the same as the class schedule code it eliminates it
            if deleteType in courseList[i].classScheduleList:
                courseList[i].classScheduleList.remove(deleteType)
                print("Desasignación Correcta.\n")
            else:
                print("No haz Pulsado una Opción Correcta o el Horario no ha sido Asignado.")
    SetCourseList(courseList)
#This function shows the options
def ClassScheduleToCourseMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1...Asignar un Horario a un Curso.\n"
          "\t2...Desasignar un Horario a un Curso.\n"
          "\t3...Visualizar las asignaciones del Curso.\n"
          "\t0...Volver al Menú Operativo.")
#This function is chosen the option
def ClassScheduleToCourseMenuOptions():
    while True:
        ClassScheduleToCourseMenu()
        optionsEntry = input("\nIngrese la opción a Escoger: ")
        if optionsEntry== "1":
            AddClassScheduleToCourses()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "2":
            DeleteClassScheduleToCourse()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "3":
            ShowAsignationToCourses()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "0":
            break
        else:
            input("\nNo has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")
ClassScheduleToCourseMenuOptions()