import logging

import uvicorn
from fastapi import FastAPI

from fastapi_poetry_template.database import Base, engine  # old import
from fastapi_poetry_template.example_entity.router import router as example_router
from fastapi_poetry_template.utils.logging.logger import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI()
app.include_router(example_router)


@app.get("/")
def root():
    logger.info("Liveness check success")
    return "Server is running..."


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    uvicorn.run("server:app", host="127.0.0.1", port=6000, reload=True)
