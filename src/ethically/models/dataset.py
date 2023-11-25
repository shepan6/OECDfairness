# from ethically.models.report import Report, EthicsReport
from typing import Any

from pandas import DataFrame
from pydantic import BaseModel, ConfigDict


class Dataset(BaseModel):
    data: DataFrame = None
    version: str = None
    predictor: str
    model_config = ConfigDict(arbitrary_types_allowed=True)

    # TODO: Include validator for predictor to chcek if in data

    # def _create_ethics_report() -> EthicsReport:
    #     pass
        