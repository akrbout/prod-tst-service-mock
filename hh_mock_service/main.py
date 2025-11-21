import logging
from pathlib import Path
import pandas as pd
import numpy as np
from fastapi import FastAPI, APIRouter
from catboost import CatBoostRegressor
from sentence_transformers import SentenceTransformer

from hh_mock_service.schemas import HHInputSchema, SalaryOutputSchema

app = FastAPI()
main_router = APIRouter(prefix="/api")

MODEL_FROM_PATH = Path(__file__).parent.parent / "models" / "catboost_from_rub.cbm"
MODEL_TO_PATH = Path(__file__).parent.parent / "models" / "catboost_to_rub.cbm"
EMBEDDING_MODEL_PATH = Path(__file__).parent.parent / "models" / "sentence_transformer_model"

# Загружаем CatBoost модели
model_from = CatBoostRegressor()
model_from.load_model(str(MODEL_FROM_PATH))

model_to = CatBoostRegressor()
model_to.load_model(str(MODEL_TO_PATH))

# Загружаем Embedding модель
embedding_model = SentenceTransformer(str(EMBEDDING_MODEL_PATH))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def prepare_features(input_data: HHInputSchema) -> pd.DataFrame:
    skills_count = len(input_data.key_skills) if input_data.key_skills else 0
    description_len = len(input_data.vacancy_description) if input_data.vacancy_description else 0
    has_location = 1 if input_data.location_lat or input_data.location_lon else 0

    skills_text = ', '.join([s.strip() for s in input_data.key_skills]) if input_data.key_skills and len(input_data.key_skills) > 0 else 'no skills'

    skills_embedding = embedding_model.encode(skills_text)

    features = {
        'profession_id': input_data.profession_id or 0,
        'skills_count': skills_count,
        'description_len': description_len,
        'has_location': has_location,
        'accept_temporary': int(input_data.accept_temporary) if input_data.accept_temporary is not None else 0,
    }

    for i, emb_value in enumerate(skills_embedding):
        features[f'skill_emb_{i}'] = float(emb_value)

    features['experience'] = input_data.experience.value if input_data.experience else 'noExperience'
    features['schedule'] = input_data.schedule.value if input_data.schedule else 'flexible'
    features['work_hours'] = input_data.work_hours.value if input_data.work_hours else 'other'

    return pd.DataFrame([features])

@main_router.post("/predict")
async def predict(input: HHInputSchema) -> SalaryOutputSchema:
    logger.info(f"Processing HH prediction request")

    try:
        features = prepare_features(input)

        salary_from = model_from.predict(features)[0]
        salary_to = model_to.predict(features)[0]

        logger.info(f"Predicted salary: {salary_from:.2f} - {salary_to:.2f} RUB")

        return SalaryOutputSchema(min=float(salary_from), max=float(salary_to))
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        return SalaryOutputSchema(min=50000.0, max=100000.0)

app.include_router(main_router)
