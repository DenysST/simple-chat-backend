from dataclasses import dataclass

class PersonClassic:
    last_name: str

    def __init__(self, name, age):
        self.name = name
        self.age = age



@dataclass
class Person:
    name: str
    age: int
    height: float

