import datetime
from enum import StrEnum, auto

from pydantic import BaseModel, ConfigDict


class ExperienceTypeEnum(StrEnum):
    between_1_And_3 = "between1And3"
    no_experience = "noExperience"
    between_3_and_6 = "between3And6"
    more_than_6 = "moreThan6"


class ScheduleTypeEnum(StrEnum):
    FIVE_ON_TWO_OFF = auto()
    TWO_ON_TWO_OFF = auto()
    OTHER = auto()
    SIX_ON_ONE_OFF = auto()
    FLEXIBLE = auto()
    THREE_ON_THREE_OFF = auto()
    FOUR_ON_TWO_OFF = auto()
    ONE_ON_THREE_OFF = auto()
    FOUR_ON_FOUR_OFF = auto()
    WEEKEND = auto()
    FOUR_ON_THREE_OFF = auto()
    THREE_ON_TWO_OFF = auto()
    ONE_ON_TWO_OFF = auto()
    TWO_ON_ONE_OFF = auto()


class WorkHoursTypeEnum(StrEnum):
    HOURS_10 = auto()
    HOURS_4 = auto()
    HOURS_8 = auto()
    HOURS_7 = auto()
    HOURS_12 = auto()
    OTHER = auto()
    HOURS_6 = auto()
    HOURS_11 = auto()
    HOURS_3 = auto()
    HOURS_9 = auto()
    HOURS_2 = auto()
    FLEXIBLE = auto()
    HOURS_24 = auto()
    HOURS_5 = auto()


class SalaryOutputSchema(BaseModel):
    min: float
    max: float

class SimilarSchema(BaseModel):
    company_id: int
    vacancy_id: int

class HHInputSchema(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "company_nm": "Яндекс",
                "vacancy_nm": "Python Backend Developer",
                "experience": "between3And6",
                "schedule": "five_on_two_off",
                "work_hours": "hours_8",
                "location": "Москва",
                "vacancy_description": "Разработка и поддержка высоконагруженных backend-сервисов на Python. Работа с микросервисной архитектурой, PostgreSQL, Redis, Kafka. Участие в проектировании новых функций и оптимизации существующих.",
                "key_skills": ["Python", "Django", "PostgreSQL", "Redis", "Docker", "Git"],
                "accept_temporary": False,
                "metro_line_nm": "Сокольническая линия",
                "metro_station_nm": "Красные Ворота",
                "location_lat": 55.755819,
                "location_lon": 37.617644,
                "profession_id": 96
            }
        }
    )

    company_nm: str | None = None
    vacancy_nm: str | None = None
    experience: ExperienceTypeEnum | None = None
    schedule: ScheduleTypeEnum | None = None
    work_hours: WorkHoursTypeEnum | None = None
    location: str | None = None
    vacancy_description: str | None = None
    key_skills: list[str] | None = None
    accept_temporary: bool | None = None
    metro_line_nm: str | None = None
    metro_station_nm: str | None = None
    location_lat: float | None = None
    location_lon: float | None = None
    profession_id: int | None = None
