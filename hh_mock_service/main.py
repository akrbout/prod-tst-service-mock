import logging
from fastapi import FastAPI, APIRouter

from hh_mock_service.schemas import HHInputSchema, SalaryOutputSchema

app = FastAPI()
main_router = APIRouter(prefix="/api")

@main_router.post("/process")
async def process_input(input: HHInputSchema) -> SalaryOutputSchema:
    logging.info("Schema comeeeeee")

app.include_router(main_router)