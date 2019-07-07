import os
import json
import time


def objectsave(init_func_argument) :
    def inner_function(self, *args) :
        init_func_argument(self, *args)
        self.id = str(time.time())
    return inner_function

class Person() :

    @objectsave
    def __init__(self, first_name, last_name, age) :
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = first_name + ' ' + last_name



object = Person('John', 'Doe', 25)

print(object.id)
print(object.__dict__)
