import logging
from fastapi import FastAPI, APIRouter

from tk_mock_service.schemas import TkInputSchema, TkOutputSchema

app = FastAPI()
main_router = APIRouter(prefix="/api")

@main_router.post("/process")
async def process_input(input: TkInputSchema) -> TkOutputSchema:
    logging.info("Schema comeeeeee")

app.include_router(main_router)
