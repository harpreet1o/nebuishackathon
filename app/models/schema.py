from pydantic import BaseModel

class FieldSpec(BaseModel):
    name: str 
    type: str
    required: bool = False

class TargetSchema(BaseModel):
    fields: list[FieldSpec]
    