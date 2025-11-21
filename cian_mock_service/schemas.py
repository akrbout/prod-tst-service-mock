import datetime
from enum import StrEnum, auto

from pydantic import BaseModel, Field


class CianOutputSchema(BaseModel):
    price: float = Field()


class TypeNameTypeEnum(StrEnum):
    sale = auto()
    rent = auto()


class CianInputSchema(BaseModel):
    ad_id: str
    type_nm: TypeNameTypeEnum
    category_nm: str
    title: str
    full_address_txt: str
    total_area: float
    floor_no: int
    desc_txt: str | None = None
    price_amt: float
    sq_price_amt: float
    url_txt: str
    year_built: int | None
    ad_dttm: datetime.datetime
    create_dttm: datetime.datetime | None = None
    city_nm: str
    latitude: float
    longitude: float
