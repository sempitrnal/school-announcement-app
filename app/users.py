

from announcement import *
import hashlib
import string
from enum import Enum
from singleton import Singleton


class StudentType(Enum):
    Elementary = 1
    High_School = 2
    College = 3


class Person():
    key = 'brow'

    def __init__(self, fn, ln, age, id) -> None:
        nfn = " ".join([a[0].upper() + a[1:].lower()
                       for a in fn.split(" ") if a != ""])
        nln = " ".join([a[0].upper() + a[1:].lower()
                       for a in ln.split(" ") if a != ""])
        self.id = id
        self.__firstName = nfn
        self.__lastName = nln
        self.__age = age
        self.__pword = hashlib.md5(((nln + str(12345))+self.key).encode())

    def set_pword(self, newPword: string):
        self.__pword = hashlib.md5((newPword+self.key).encode())

    def getId(self) -> int:
        return self.id

    def getName(self) -> str:
        return f"{self.__firstName} {self.__lastName}"

    def get_fname(self) -> str:
        return self.__firstName

    def get_age(self) -> int:
        return self.__age

    def get_pword(self) -> str:
        return self.__pword.hexdigest()


class Observer:
    def __init__(self, subject):
        self.subject = subject
        subject.attach(self)

    def update(self):
        pass


class RegistrarAdmin(Person, metaclass=Singleton):
    def __init__(self, fn, ln, age, id) -> None:
        super().__init__(fn, ln, age, id)


class UniversityPresident(Person, metaclass=Singleton):
    def __init__(self, fn, ln, age, id) -> None:
        super().__init__(fn, ln, age, id)

    def createMemo(self, announcement, s) -> None:
        s.relayMemo(announcement)


class UniversitySecretary(Person, Subject, metaclass=Singleton):
    def __init__(self, fn, ln, age, id) -> None:
        super().__init__(fn, ln, age, id)

    def relayMemo(self, a):
        AnnouncementManager().add_announcement(a)

    def announce(self, announcement) -> None:
        AnnouncementManager().add_announcement(announcement)


class Student(Person, Observer):
    def __init__(self, fn, ln, age, type, id) -> None:
        super().__init__(fn, ln, age, id)
        self.type = StudentType(type).name

    def getId(self) -> string:
        return super().getId()

    def getName(self) -> string:
        return super().getName()

    def get_type(self) -> string:
        s = " ".join(self.type.split("_"))
        return s

    def viewAnnouncements(self):
        AnnouncementManager().get_announcements_by_type(self.get_type())

    def update(self, announcement):
        print(
            f"{self.getName()} received an announcement: {announcement.to_string()}")
