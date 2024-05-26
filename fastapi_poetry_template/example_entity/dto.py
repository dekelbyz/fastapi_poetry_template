from pydantic import BaseModel, Field


class CreateExampleDataDto(BaseModel):
    status: str = Field(..., min_length=2, max_length=30, description='City')
