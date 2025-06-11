from pydantic import BaseModel, ConfigDict, ValidationError


class Model(BaseModel):
    model_config = ConfigDict(extra="allow")

    field_1: int = 0

m = Model (extra_field = "Data")
print(type(m.model_extra))
