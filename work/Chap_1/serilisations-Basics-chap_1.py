from pydantic import BaseModel, ValidationError

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int


galois = Person( first_name="Evariste", last_name="Galois", age=20 )
newton = Person( first_name="Isaac", last_name="Newton", age=84 )

print(newton.__dict__)

print(galois.model_dump())
print(galois.model_dump(exclude={'first_name', 'last_name'}))
print(galois.model_dump_json(include={'first_name', 'last_name'}, indent=4))