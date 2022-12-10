from enum import Enum
import string
from singleton import Singleton


class AnnouncementType(Enum):
    Holiday = 1
    Elementary = 2
    High_School = 3
    College = 4
    Blue_Memo = 5


class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, a):
        [observer.update(a) 
         for observer in self.observers 
         if observer.type == a.get_type() 
         or a.get_type() == AnnouncementType.Holiday.name 
         or a.get_type() == AnnouncementType.Blue_Memo.name]


class Announcement:

    def __init__(self, name, type, description) -> None:
        self._name = name
        self._type = AnnouncementType(type).name
        self._description = description

    def to_string(self) -> string:
        s = " ".join(self._type.split("_"))
        return f"\n\n------- {self._name} -------\n\nType: {s}\n\n{self._description}\n"

    def get_name(self) -> string:
        return self._name

    def get_type(self) -> string:
        return self._type


class AnnouncementManager(Subject, metaclass=Singleton):

    def __init__(self) -> None:
        super().__init__()
        self.__announcements = []

    def add_announcement(self, announcement):
        self.__announcements.append(announcement)
        super().notify(announcement)

    def get_announcements(self):
        print("\n".join([announcement.to_string()
              for announcement in self.__announcements]))

    def get_announcements_by_type(self, type):
        print("\n".join([announcement.to_string() 
                         for announcement in self.__announcements 
                         if announcement.get_type() == type 
                         or announcement.get_type() == AnnouncementType.Holiday.name 
                         or announcement.get_type() == AnnouncementType.Blue_Memo.name]))
