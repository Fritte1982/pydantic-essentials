from pprint import pprint
from datetime import date
from pydantic import BaseModel

class Automobile(BaseModel):
    manufacturer: str
    series_name: str
    type_: str
    is_electric: bool = False
    manufactured_date: date
    base_msrp_usd: float
    vin: str
    number_of_doors: int = 4
    registration_country: str = None
    license_plate: str = None


data = {
    "manufacturer": "BMW",
    "series_name": "M4",
    "type_": "Convertible",
    "is_electric": False,
    "manufactured_date": "2023-01-01",
    "base_msrp_usd": 93_300,
    "vin": "1234567890",
    #  "numbers_of_doors": 2,
    "registration_country": "France",
    "license_plate": "AAA-BBB",
}

car = Automobile.model_validate(data)

json_schema = car.model_json_schema()

pprint(json_schema)