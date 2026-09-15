from pydantic import BaseModel


class TransformationMapping(BaseModel):
    source: str
    target: list[str]
    operation: str
    confidence: float


class TransformationPlan(BaseModel):
    mappings: list[TransformationMapping]