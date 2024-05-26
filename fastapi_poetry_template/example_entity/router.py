from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.orm import Session

from fastapi_poetry_template.example_entity.service import ExampleService
from fastapi_poetry_template.database import get_db
from fastapi_poetry_template.example_entity import dto
from fastapi_poetry_template.utils.logging.logger import setup_logging
import logging
setup_logging()
logger = logging.getLogger(__name__)

db_dependency = Annotated[Session, Depends(get_db)]

router = APIRouter(prefix='/example', tags=['example'])

service = ExampleService()


@router.get('/')
def example():
    return service.example()


@router.post('/create-data', status_code=201)
def create_example_data(example_data_details: dto.CreateExampleDataDto, db: db_dependency):
    try:
        logger.info(f'Creating example data request')

        db_example_entity = service.create_example_data(
            example_data_details=example_data_details,
            db=db
        )
        logger.info(f'Created example data successfully. status is now "{
                    db_example_entity.status}"')

        return db_example_entity
    except Exception as e:
        logger.error(e)
