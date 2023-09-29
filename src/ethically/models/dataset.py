# from ethically.models.report import Report, EthicsReport
from ethically.models.measure import Metric
from ethically.models.measure.representative import DatasetDivergenceMetric
from pydantic import BaseModel
from typing import Any


class Dataset(BaseModel):
    data: Any = None
    measures: list[Metric] = []

    def measure(self, metrics:list[str]) -> None:
        self.measures += [{
            "dataset-divergence": DatasetDivergenceMetric()
        }[metric]._compute() for metric in metrics]

    def is_ethical(cols: list[str]) -> bool:
        pass

    def is_representative(cols: list[str]) -> bool:
        pass

    # def _create_ethics_report() -> EthicsReport:
    #     pass
