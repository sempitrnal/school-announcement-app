from users import *
from announcement import *
from registrar import *
from singleton import *


class School(metaclass=Singleton):
    _uni_pres = UniversityPresident("John", "Doe", 50)
    _uni_sec = UniversitySecretary("Jane", "Doe", 50)
    _am = AnnouncementManager()
    _reg = Registrar()

    def start(self, choice):
        match choice:
            case 1:  # student admission

                fn = input("Enter student's first name: ")

                ln = input("Enter student's last name: ")
                age = int(input("Enter student's age: "))
                type = int(
                    input("Enter student's type [1] Elementary, [2] High School, [3] College: \n"))

                self._reg.add_student(Student(fn, ln, age, type))

            case 2:
                self._reg.get_students()

            case 3:  # create blue memo
                name = input("Enter name of memo: ")
                content = input("Enter content of memo: \n\n>")
                a = Announcement(name, 5, content)
                self._uni_pres.createMemo(a, self._uni_sec)
            case 4:
                name = input("Enter name of Announcement: ")
                content = input("Enter content of Announcement:\n\n> ")
                type = int(input(
                    "Enter type of Announcement [1] Holiday, [2] Elementary, [3] High School, [4] College: \n\n Type: "))
                a = Announcement(name, type, content)
                self._uni_sec.announce(a)
            case 5:
                self._am.get_announcements()
            case other:
                print("Invalid choice")
