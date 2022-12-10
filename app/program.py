from users import *
from announcement import *
from registrar import *
from school import *
p = UniversityPresident("Elmer", "Doe", 20)

s = UniversitySecretary("John", "Doe", 20)
s1 = Student("John", "Doe", 18, 1)

s2 = Student("Jane", "Doe", 19, 2)

choice = -1

while (choice != 0):
    choice = int(input("Enter choice: "))
    School().start(choice)
