import unittest
from registrar import *
from announcement import *
from login import *
from school import *
from singleton import *
from users import *
from abc import abstractmethod


class UnitTesting(unittest.TestCase):
    # The Arrange section of a unit test method initializes objects and sets the value of the data that is passed to the method under test. The Act section invokes the method under test with the arranged parameters. The Assert section verifies that the action of the method under test behaves as expected.

    def test_getStudent_should_update_password(self):
        #Arrange
        expectedNewPass="John12345"

        #Act
        logged: Person = None
        login = Login()
        logged = login.login
        logged.set_pword("John12345")

        #Assert
        self.assertEqual(logged.get_pword, expectedNewPass)


    def test_getRegistrar_should_add_student(self):
    #Arrange
        expectedStudent=Student("Johnny", "Silverhand", 22, 3, 0)
    #Act
        registrar = Registrar()
        registrar.add_student(expectedStudent)
    # Assert
        self.assertEqual(registrar.get_students_list, expectedStudent)

    def test_getRegistrar_should_remove_student(self):
    #Arrange
        expectedOutput=""
    #Act
        registrar = Registrar()
        registrar.__students.remove("Johnny Silverhand")
    # Assert
        self.assertEqual(registrar.__students, expectedOutput)
    
    def test_getRegistrar_should_create_announcement(self):
        #Arrange
        expectedAnnouncementName="Intrams"
        expectedContent="Starts tomorrow"
        expectedType="College"

        #Act
        a = Announcement("Intrams", 4, "Starts tomorrow")
        
        #Assert
        self.assertEqual(a._name, expectedAnnouncementName)
        self.assertEqual(a._description, expectedContent)
        self.assertEqual(a._type, expectedType)

    def test_getUniPresident_should_create_blue_memo(self):
        #Arrange
        expectedName="Intrams"
        expectedContent="No classes"
        expectedType="College"
        
        #Act
        a = Announcement("Intrams", 4, "No classes")

        #Assert
        self.assertEqual(a._name, expectedName)
        self.assertEqual(a._description, expectedContent)
        self.assertEqual(a._type, expectedType)

if __name__ == '__main__':
        unittest.main()