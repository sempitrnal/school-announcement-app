from users import *
from announcement import *
from registrar import *
from school import *


choice = -1

while (choice != 0):
    choice = int(input("Enter choice: "))
    School().start(choice)
