# from ethically.models.report import Report, EthicsReport
from typing import Any

from pydantic import BaseModel


class Dataset(BaseModel):
    data: Any = None
    version: str = None
    predictor: str

    # TODO: Include validator for predictor to chcek if in data

    # def _create_ethics_report() -> EthicsReport:
    #     pass
