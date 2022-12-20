from announcement import *
from person import *
from singleton import Singleton

class UniversitySecretary(Person, Subject, metaclass=Singleton):
    def __init__(self, fn, ln, age, id) -> None:
        super().__init__(fn, ln, age, id)

    def relayMemo(self, a):
        AnnouncementManager().add_announcement(a)

    def announce(self, announcement) -> None:
        AnnouncementManager().add_announcement(announcement)