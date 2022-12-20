from users import *
from announcement import *
from registrar import *
from singleton import *


class School(metaclass=Singleton):
    _uni_pres = UniversityPresident("John", "Doe", 50, 1)
    _uni_sec = UniversitySecretary("Jane", "Doe", 50, 1)
    _uni_regAdmin = RegistrarAdmin("Steve", "Doe", 30, 1)
    _am = AnnouncementManager()
    _reg = Registrar()

    def getRegistrar(self) -> Registrar:
        return self._reg

    def getRegAdmin(self) -> RegistrarAdmin:
        return self. _uni_regAdmin

    def getAnnouncementManager(self) -> AnnouncementManager:
        return self._am

    def getUniPres(self) -> UniversityPresident:
        return self._uni_pres

    def getUniSec(self) -> UniversitySecretary:
        return self._uni_sec


class SchoolManager(School):
    def start(self, logged: Person):
        choice = -1
        match logged.__class__.__name__:
            case Student.__qualname__:
                while (choice != 0):
                    print(
                        f"[1] Update Password\n[2] View Recent Announcements\n[3] View All {logged.get_type()} Level Announcement \n\n[0] Logout")
                    choice = int(input("What do you want to do? "))
                    match choice:
                        case 1:
                            oldPass = input("Enter old password: ")
                            if (hashlib.md5((oldPass+'brow').encode()).hexdigest() == logged.get_pword()):
                                newPass = input("Enter New Pass: ")
                                logged.set_pword(newPass)
                                print(logged.get_pword())
                                print("Successfully changed your password!\n\n")
                            else:
                                print("Wrong Old Password!\n\n")
                        case 2:
                            super().getAnnouncementManager().get_announcements()
                        case 3:
                            super().getAnnouncementManager().get_announcements_by_type(logged.get_type())
                        case 0: print("Logging you out...")
                        case _: print("Wrong input!")
                return -1
            case RegistrarAdmin.__qualname__:
                while (choice != 0):
                    print(
                        "[1] Add Student\n[2] View Student List\n[3] Remove Student\n[4] Create Announcement\n[5] View Recent Announcements \n\n[0] Logout")
                    choice = int(input("What do you want to do? "))
                    match choice:

                        case 1:  # student admission
                            currentIdCount = 0

                            # self._reg.add_student(Student("John", "Doe", 21, 1, currentIdCount+1))
                            currentIdCount = super().getRegistrar().get_students_list()[len(super().getRegistrar(
                            ).get_students_list())-1].getId() if len(super().getRegistrar().get_students_list()) > 0 else 0
                            logged: Person() = None
                            fn = input("Enter student's first name: ")
                            ln = input("Enter student's last name: ")
                            age = int(input("Enter student's age: "))
                            studType = int(
                                input("Enter student's type [1] Elementary, [2] High School, [3] College: \n"))
                            super().getRegistrar().add_student(Student(fn, ln, age, studType, currentIdCount))

                        case 2:
                            super().getRegistrar().get_students()
                        case 3:
                            super().getRegistrar().get_students()
                            removeStudent = int(
                                input("Enter the ID from the list you wish to remove from the list: "))
                            super().getRegistrar().remove_student(removeStudent)

                        case 4:
                            name = input("Enter name of Announcement: ")
                            content = input(
                                "Enter content of Announcement:\n\n> ")
                            studType = int(input(
                                "Enter type of Announcement [1] Holiday, [2] Elementary, [3] High School, [4] College: \n\n Type: "))
                            a = Announcement(name, studType, content)
                            super().getUniSec().announce(a)

                        case 5:
                            super().getAnnouncementManager().get_announcements()

                        case other:
                            print("Invalid choice")
                return -1

            case UniversityPresident.__qualname__:
                while (choice != 0):
                    print(
                        f"[1] Create Blue Memo\n[2] View Recent Announcements\n\n[0] Logout")
                    choice = int(input("What do you want to do? "))
                    match choice:
                        case 1:  # create blue memo
                            name = input("Enter name of memo: ")
                            content = input("Enter content of memo: \n\n>")
                            a = Announcement(name, 5, content)
                            self._uni_pres.createMemo(a, self._uni_sec)
                            pass
                        case 2:
                            super().getAnnouncementManager().get_announcements()
                        case 0: print("Logging you out...")
                        case _: print("Wrong input!")
                return -1
            case _:
                print('Wrong Input!')
