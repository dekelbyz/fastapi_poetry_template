from sqlalchemy.orm import Session

from fastapi_poetry_template.example_entity import dto
from fastapi_poetry_template.example_entity.model import Example


class ExampleService:
    def example(self):
        return "Hello World!"

    def create_example_data(
        self, example_data_details: dto.CreateExampleDataDto, db: Session
    ):
        example_db_entity = Example(**example_data_details.model_dump())
        db.add(example_db_entity)
        db.commit()
        return example_db_entity
