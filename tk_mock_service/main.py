import logging
from pathlib import Path
import pandas as pd
from fastapi import FastAPI, APIRouter
from catboost import CatBoostRegressor, Pool

from tk_mock_service.schemas import TkInputSchema, TkOutputSchema

app = FastAPI(
    title="Delivery Predict Service",
    description="Сервис для кейса `Тариф, я выбираю тебя!`",
)
main_router = APIRouter(prefix="/api")

MODEL_PATH = Path(__file__).parent.parent / "models" / "major_express_catboost_model.cbm"
CATEGORICAL_FEATURES = ['departure', 'destination', 'destination_tk', 'tariff']

model = CatBoostRegressor()
model.load_model(str(MODEL_PATH))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def prepare_features(input_data: TkInputSchema) -> pd.DataFrame:
    departure = input_data.departure or "Москва"
    destination = input_data.destination or "Шишино"
    destination_tk = input_data.destination_tk or "Шишино(Белгородская обл., Белгородский р-н)"
    tariff = input_data.tariff or "Экспресс"
    weight_kg = input_data.weight_kg or 10.0
    duration_min = input_data.duration_min or 2
    duration_max = input_data.duration_max or 2
    duration_avg = (duration_min + duration_max) / 2

    features = pd.DataFrame([{
        'duration_min': duration_min,
        'duration_max': duration_max,
        'duration_avg': duration_avg,
        'departure': departure,
        'destination': destination,
        'destination_tk': destination_tk,
        'tariff': tariff,
        'weight_kg': weight_kg
    }])

    return features

@main_router.post("/process")
async def process_input(input: TkInputSchema) -> TkOutputSchema:
    try:
        features = prepare_features(input)
        pool = Pool(features, cat_features=CATEGORICAL_FEATURES)
        price = model.predict(pool)[0]

        logger.info(f"Predicted price: {price:.2f} RUB")

        return TkOutputSchema(price=float(price))
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        return TkOutputSchema(price=8000.0)

app.include_router(main_router)
