from pydantic import ValidationError
from dataclasses import dataclass


@dataclass
class Model:
    language: str
    version: str
    year: int

from pydantic import BaseModel
class Model(BaseModel):
    language: str
    version: str
    year: int

model_obct = Model(language="python", version="1.0.0", year=2020)

new_model = Model.model_validate(
    {
        "language": "python",
        "version": "3, 12, 0",
        "year": 2025

    }
)

print(new_model)

### Creating a Pydantic Model

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int

    @property
    def display_name(self):
        return f"{self.first_name} {self.last_name}"

p = Person(first_name="Evariste", last_name="Galois", age=20)
print(str(p))
print(repr(p))
print(Person.model_fields)  # Aus obj.model_fields wird jetzt class.model_fields

try:
    p2 = Person(first_name="Evariste", last_name="Galois")
except ValidationError as e:
    print(e)

print(p.display_name)

try:
    p2 = Person(first_name="Evariste", last_name="Galois", age="String")
except ValidationError as e:
    print(e)

p3 = Person(first_name="Isaac", last_name="Newton", age=84)

data = {
    "first_name": "Isaac",
    "last_name": "Newton",
    "age": 84
}

pers_isaac = Person(**data)
print(pers_isaac)
isaac_from_dict = Person.model_validate(data)
print(isaac_from_dict)

data_json = '''
{
    "first_name": "Isaac",
    "last_name": "Newton",
    "age": 84
}
'''

isaac_from_json = Person.model_validate_json(data_json)
print(isaac_from_json)