#Imports
from ClassLogic.StudentLogic import *
from ClassLogic.CampusLogic import*
from ClassLogic.TeacherLogic import *
from ClassLogic.ClassroomsLogic import *
from ClassLogic.ClassScheduleLogic import *
from ClassLogic.CourseLogic import *
from ClassLogic.CareerLogic import *
#This function shows the options
def Menu():
    print("\nSelecciona una Opción.\n"
          "\t1...Opciones Estudiante.\n"
          "\t2...Opciones Docentes.\n"
          "\t3...Opciones Carreras.\n"
          "\t4...Opciones Cursos.\n"
          "\t5...Opciones Recintos.\n"
          "\t6...Opciones Aulas.\n"
          "\t7...Opciones Horarios.\n"
          "\t0...Volver al Menú Principal.")
#This function is chosen the option
def MenuOptions():
    while True:
        Menu()
        optionsEntry = input("\nIngrese la Opción a Escoger: ")
        if optionsEntry == "1":
            StudentMenuOptions()
            input("\npulsa una tecla para continuar.")
        elif optionsEntry == "2":
            TeacherMenuOption()
            input("\npulsa una tecla para continuar.")
        elif optionsEntry == "3":
            CareerMenuOptions()
            input("\npulsa una tecla para continuar.")
        elif optionsEntry == "4":
            CourseMenuOptions()
            input("\npulsa una tecla para continuar.")
        elif optionsEntry == "5":
            CampusMenuOptions()
            input("\npulsa una tecla para continuar.")
        elif optionsEntry == "6":
            ClassRoomsMenuOptions()
            input("\npulsa una tecla para continuar.")
        elif optionsEntry == "7":
            ClassScheduleMenuOptions()
            input("\npulsa una tecla para continuar.")
        elif optionsEntry == "0":
            break
        else:
            input("\nNo has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú.")