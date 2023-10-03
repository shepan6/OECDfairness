# from ethically.models.report import Report, EthicsReport
from ethically.models.measure.metric import Metric, Metrics, DatasetDivergenceMetric
from pydantic import BaseModel
from typing import Any


class Dataset(BaseModel):
    data: Any = None
    measures: Metrics = Metrics()

    def measure(self, metric_names: list[str] = []) -> None:
        # NOTE: passing over dataset object to metric compute??
        # NOTE: Get to such a way that we do not need to compute then append?
        self.measures.compute_metrics_from_metric_names(metric_names=metric_names)

    def is_ethical(cols: list[str]) -> bool:
        pass

    def is_representative(cols: list[str]) -> bool:
        pass

    # def _create_ethics_report() -> EthicsReport:
    #     pass
