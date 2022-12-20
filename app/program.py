from users import *
from announcement import *
from registrar import *
from school import *
from login import *

choice = -1
logged: Person = None
school = School()
schoolManager = SchoolManager()
login = Login()

school.getRegistrar().add_student(Student("Kidd", "Doe", 10, 1, 0))
school.getRegistrar().add_student(Student("Tin", "Doe", 16, 2, 1))
school.getRegistrar().add_student(Student("Collei", "Doe", 21, 3, 2))
while (choice != 0):
    print("\n\nCEBU INSTITUTE OF TECHNOLOGY - UNIVERSITY")
    print(
        "Welcome!\nAre you a:\n[1] Student\n[2] Registrar Admin\n[3] University President\n\n[0] Exit")
    choice = int(input("Input Choice: "))
    if (choice != 0):
        logged = login.login(school, choice)
        if (logged != None):
            choice = schoolManager.start(logged)
