from announcement import *
import hashlib
import string
from enum import Enum


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