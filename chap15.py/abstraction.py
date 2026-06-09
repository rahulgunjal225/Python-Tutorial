
# Abstraction means showing only the important information and hiding the internal details.

# DOES NOT EXIST IN PYTHON BUT WE CAN ACHIEVE IT USING A LIBRARY


from abc import ABC , abstractmethod

class enforce(ABC):
    @abstractmethod
    def enginestart():
        pass


class bike(enforce):
    def enginestart():
        pass


class car(enforce):
    def enginestart():
        pass

class truck(enforce):
    def enginestart():
        pass


obj1 = bike()
obj2 = car()
obj3 = truck()