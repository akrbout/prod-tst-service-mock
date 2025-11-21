import datetime
from enum import StrEnum, auto
from typing import Literal

from pydantic import BaseModel, Field


class TkOutputSchema(BaseModel):
    price: float = Field()


class TkInputSchema(BaseModel):
    departure: str
    destination_tk: str
    tariff: Literal["Экспресс", "Сборный груз (Дверь - Дверь)", "Сборный груз (Терминал - Дверь)", "Сборный груз (Дверь - Терминал)"]
    weight_kg: float
    duration_min: int
    duration_max: int

