from abc import ABC,abstractmethod

class Employee(ABC):

    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    @abstractmethod
    def calculate_salary(self):
        pass

    @property
    def salary(self):
        return self.__salary

    def display_details(self):
        print(f'Name : {self.name}')
        print(f'Salary : {self.salary}')