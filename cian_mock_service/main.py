import logging
from fastapi import FastAPI, APIRouter

from cian_mock_service.schemas import CianInputSchema, CianOutputSchema

app = FastAPI()
main_router = APIRouter(prefix="/api")

@main_router.post("/process")
async def process_input(input: CianInputSchema) -> CianOutputSchema:
    logging.info("Schema comeeeeee")

app.include_router(main_router)