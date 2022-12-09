from abc import abstractmethod, ABCMeta
import string
from enum import Enum

class StudentType(Enum):
  Elementary = 1
  HighSchool = 2
  College = 3

class Person():
  def __init__(self,fn,ln,age) -> None:
   self.__firstName = fn
   self.__lastName = ln
   self.__age = age
  
  def getName(self) -> string:
    return f"{self.__firstName} {self.__lastName}"
  
class Singleton (type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]








class UniversityPresident(Person, metaclass=Singleton):
  def __init__(self, fn, ln, age) -> None:
     super().__init__(fn, ln, age)
     
  def createMemo():
    return
  
  
  
  
  
  
  
class UniversitySecretary(Person, metaclass=Singleton):
  announcements = []
  def __init__(self, fn, ln, age) -> None:
    super().__init__(fn, ln, age)
  
  def relayMemo():
    return
  
  def announce():
    return







class Student(Person):
  def __init__(self, fn, ln, age,type) -> None:
    super().__init__(fn, ln, age)
    self.type = StudentType(type).name
  
  def getName(self) -> string:
    return super().getName()
  
  def viewAnnouncements(self):
    pass
  

