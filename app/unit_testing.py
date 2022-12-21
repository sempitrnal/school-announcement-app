import unittest
from registrar import *
from announcement import *
from login import *
from school import *
from singleton import *

from abc import abstractmethod


class UnitTesting(unittest.TestCase):
    # The Arrange section of a unit test method initializes objects and sets the value of the data that is passed to the method under test. The Act section invokes the method under test with the arranged parameters. The Assert section verifies that the action of the method under test behaves as expected.

    def test_getRegistrar_should_add_student(self):
        # Arrange
        student = Student("Johnny", "Silverhand", 22, 3, 0)
    # Act
        registrar = Registrar()

        registrar.add_student(student)
        expectedStudent = [
            stud for stud in registrar.get_students_list() if stud == student][0] #this fetches the value of the first index in the list

    # Assert
        self.assertEqual(student, expectedStudent)

    def test_getRegistrar_should_remove_student(self):
        # Arrange
        registrar = Registrar()
        student = [
            stud for stud in registrar.get_students_list() if stud.getName() == "Johnny Silverhand"][0]
        # Act
        registrar.remove_student(student)
        expected = registrar.get_students_list().__contains__(
            student)  # check if the student is not in the list anymore
    # Assert
        # assert false because after removing the student, the list should be empty
        self.assertEqual(False, expected)

    def test_getRegistrar_should_create_announcement(self):
        # Arrange
        expectedAnnouncementName = "Intrams"
        expectedContent = "Starts tomorrow"
        expectedType = "College"

        # Act
        a = Announcement("Intrams", 4, "Starts tomorrow")

        # Assert
        self.assertEqual(a._name, expectedAnnouncementName)
        self.assertEqual(a._description, expectedContent)
        self.assertEqual(a._type, expectedType)

    def test_getUniPresident_should_create_blue_memo(self):
        # Arrange
        expectedName = "Intrams"
        expectedContent = "No classes"
        expectedType = "College"

        # Act
        a = Announcement("Intrams", 4, "No classes")

        # Assert
        self.assertEqual(a._name, expectedName)
        self.assertEqual(a._description, expectedContent)
        self.assertEqual(a._type, expectedType)


if __name__ == '__main__':
    unittest.main()
