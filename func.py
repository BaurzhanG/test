class InvalidObjectType(Exception):

    def __init__(self, text):
        self.text = text


class Department:
    def __init__(self, department_name, director=None):
        self.__department_name = department_name
        if isinstance(director, Person):
            self.__director = director
        else:
            raise InvalidObjectType('director должен быть обьектом класса Person')
        self.__employees = []

    def add_employees(self, person):
        if isinstance(person, Person):
            self.__employees.append(person)
        else:
            raise InvalidObjectType("Обьект должен быть класса Person")


class Person:

    def __init__(self, name, surname, position):
        self.__name = name
        self.__surname = surname
        self.__position = position

person1 = Person('Paver', 'Durov', 'CTO')
person2 = Person('Magzhan', 'Zh', 'backend developer')
department = Department('IT', person1)
department.add_employees(person2)