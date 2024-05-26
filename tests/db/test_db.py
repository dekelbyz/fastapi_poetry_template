from sqlalchemy.orm import Session
from fastapi_poetry_template.example_entity.dto import CreateExampleDataDto
from fastapi_poetry_template.example_entity.service import ExampleService

#! This import is crucial, even though it's not directly used
from tests.mock_db import session

service = ExampleService()


def test_create_item(session: Session) -> None:
    example_data_details = CreateExampleDataDto(status='created')
    created_data = service.create_example_data(
        example_data_details=example_data_details, db=session)

    assert created_data.status == 'created'
