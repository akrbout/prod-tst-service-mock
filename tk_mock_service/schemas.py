import datetime
from enum import StrEnum, auto
from typing import Literal, Optional

from pydantic import BaseModel, Field


class TkOutputSchema(BaseModel):
    price: float = Field()


class TkInputSchema(BaseModel):
    departure: Optional[str] = None
    destination: Optional[str] = None
    destination_tk: Optional[str] = None
    tariff: Optional[Literal["Экспресс", "Сборный груз (Дверь - Дверь)", "Сборный груз (Терминал - Дверь)", "Сборный груз (Дверь - Терминал)"]] = None
    weight_kg: Optional[float] = None
    duration_min: Optional[int] = None
    duration_max: Optional[int] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "departure": "Москва",
                    "destination": "Шишино",
                    "destination_tk": "Шишино(Белгородская обл., Белгородский р-н)",
                    "tariff": "Экспресс",
                    "weight_kg": 10.0,
                    "duration_min": 2,
                    "duration_max": 2
                }
            ]
        }
    }
