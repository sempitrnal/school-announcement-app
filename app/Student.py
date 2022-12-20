from announcement import *
from person import *

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