import logging
from pathlib import Path
import pandas as pd
import math
from fastapi import FastAPI, APIRouter
from catboost import CatBoostRegressor

from cian_mock_service.schemas import CianInputSchema, CianOutputSchema

app = FastAPI(
    title="Area Offer Predict Service",
    description="Сервис для кейса `Где выгодно купить помещение?`",
)
main_router = APIRouter()

MODEL_PATH = Path(__file__).parent.parent / "models" / "catboost_cian_price.cbm"
model = CatBoostRegressor()
model.load_model(str(MODEL_PATH))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def prepare_features(input_data: CianInputSchema) -> pd.DataFrame:
    from datetime import datetime

    current_year = datetime.now().year
    building_age = current_year - input_data.year_built if input_data.year_built else 0
    desc_len = len(input_data.desc_txt) if input_data.desc_txt else 0
    has_coords = 1 if (input_data.latitude and input_data.longitude) else 0

    area = input_data.total_area if input_data.total_area else 50.0

    features = pd.DataFrame([{
        'area': area,
        'floor': input_data.floor_no if input_data.floor_no else 1,
        'building_age': building_age,
        'desc_len': desc_len,
        'has_coords': has_coords,
        'type_nm': input_data.type_nm.value if input_data.type_nm else 'sale',
        'category_nm': input_data.category_nm if input_data.category_nm else 'officeRent',
        'city_nm': input_data.city_nm if input_data.city_nm else 'Москва'
    }])

    return features

@main_router.post("/predict")
async def predict(input: CianInputSchema) -> CianOutputSchema:
    logger.info(f"Processing Cian prediction request")

    try:
        features = prepare_features(input)
        prediction = model.predict(features)[0]
        logger.info(f"Predicted price: {prediction:.2f} RUB")
        return CianOutputSchema(price=math.trunc(float(prediction)))
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        fallback_area = input.total_area if input.total_area else 50.0
        fallback_price = fallback_area * 100000
        return CianOutputSchema(price=math.trunc(fallback_price))

app.include_router(main_router)
