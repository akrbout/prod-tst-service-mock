import datetime
from enum import StrEnum, auto

from pydantic import BaseModel


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
    company_id: int
    vacancy_id: int
    company_nm: str
    vacancy_nm: str
    experience: ExperienceTypeEnum
    schedule: ScheduleTypeEnum
    work_hours: WorkHoursTypeEnum | None = None
    publication_dt: datetime.datetime
    location: str
    vacancy_description: str
    key_skills: list[str]
    accept_temporary: bool
    similar_ids: list[SimilarSchema]
    current_view_count: int
    scraped_timestamp: int
    metro_line_nm: str
    metro_station_nm: str
    location_lat: float
    location_lon: float
    profession_id: int
    accept_incomplete_resumes: bool
