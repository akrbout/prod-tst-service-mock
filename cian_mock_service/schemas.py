import datetime
from enum import StrEnum, auto

from pydantic import BaseModel, Field, ConfigDict


class CianOutputSchema(BaseModel):
    price: int = Field()


class TypeNameTypeEnum(StrEnum):
    sale = auto()
    rent = auto()


class CianInputSchema(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "type_nm": "sale",
                "category_nm": "officeRent",
                "title": "Продажа офиса 150 м² в Москве",
                "full_address_txt": "Москва, ул. Тверская, 12",
                "total_area": 150.0,
                "floor_no": 5,
                "desc_txt": "Офисное помещение площадью 150 кв.м. на 5 этаже бизнес-центра класса А. Отличная транспортная доступность, рядом метро. Современная отделка, готов к использованию.",
                "year_built": 2015,
                "city_nm": "Москва",
                "latitude": 55.755819,
                "longitude": 37.617644
            }
        }
    )

    type_nm: TypeNameTypeEnum | None = None
    category_nm: str | None = None
    title: str | None = None
    full_address_txt: str | None = None
    total_area: float | None = None
    floor_no: int | None = None
    desc_txt: str | None = None
    year_built: int | None = None
    city_nm: str | None = None
    latitude: float | None = None
    longitude: float | None = None
