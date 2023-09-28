from ethically.models.report import Report, EthicsReport
from pandas import DataFrame
from pydantic import BaseModel
from typing import Any

class Dataset(BaseModel):
    filepath: str | None
    data: Any
    raw: DataFrame
    reports: list[Report] = []

    def is_ethical(cols:list[str]) -> bool:
        pass

    def is_representative(cols:list[str]) -> bool:
        pass
    
    def _create_ethics_report() -> EthicsReport:
        pass
    
