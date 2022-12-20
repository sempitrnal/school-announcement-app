from announcement import *
from person import *
from singleton import Singleton

class RegistrarAdmin(Person, metaclass=Singleton):
    def __init__(self, fn, ln, age, id) -> None:
        super().__init__(fn, ln, age, id)