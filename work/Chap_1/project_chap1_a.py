"""Project Task chap 1"""
from datetime import date
from pprint import pprint
from pydantic import BaseModel

class Automobile(BaseModel):
    """class with needing of the task-description """
    manufacturer: str
    series_name: str
    type_: str
    is_electric: bool = False
    manufactured_date: date
    base_msrp_usd: float
    vin: str
    numbers_of_doors: int = 4
    registration_country: str | None = None
    license_plate: str | None = None

data = {
    "manufacturer": "BMW",
    "series_name": "M4",
    "type_": "Convertible",
    "is_electric": False,
    "manufactured_date": "2023-01-01",
    "base_msrp_usd": 93_300,
    "vin": "1234567890",
    "number_of_doors": 2,
    "registration_country": "France",
    "license_plate": "AAA-BBB",
}

DATA_JSON = '''
{
    "manufacturer": "BMW",
    "series_name": "M4",
    "type_": "Convertible",
    "manufactured_date": "2023-01-01",
    "base_msrp_usd": 93300,
    "vin": "1234567890"
}
'''
def main():
    """Doc-Main"""
    new_car = Automobile.model_validate(data)
    pprint(new_car.model_dump())
    car_from_json = Automobile.model_validate_json(DATA_JSON)
    pprint(car_from_json)

if __name__ == '__main__':
    main()
