from pydantic import BaseModel, RootModel
from typing import Literal
import logging


class Metric(BaseModel):
    kind: str
    name: str
    value: float = float("-inf")  # Default value that we can filter out by

    def _compute(self) -> None:
        raise NotImplementedError(
            "You have hit the base model method. The model requires a _compute() method"
        )

class Metrics(RootModel):
    root: list[Metric] = []

    @staticmethod
    def _metric_name_to_metric(metric_name: str) -> Metric:
        return {
            "dataset-divergence": DatasetDivergenceMetric()
            }[metric_name]

    def compute_metrics_from_metric_names(self, metric_names: list[str] = []) -> None:
        metrics: list[Metric] = []
        if not metric_names:
            logging.warning("There are no metrics to be computed")
            return metrics
        self.root += [self.compute_metric(metric_name=metric_name) for metric_name in metric_names]

    def compute_metric(self, metric_name: str) -> Metric:
        metric: Metric = self._metric_name_to_metric(metric_name=metric_name)
        metric._compute()
        return metric

    def __len__(self) -> int:
        return len(self.root)

    def __getitem__(self, key):
        return self.root[key]


class RepresentativeMetric(Metric):
    kind: Literal["representativeness"] = "representativeness"


class DatasetDivergenceMetric(RepresentativeMetric):
    name: Literal["dataset-divergence"] = "dataset-divergence"

    def _compute(self, features:list[str] = []):
        print("computing dataset divergence...")
        if features:
            # subset features first
            pass
        # Split data into train/test
        # Compute KL divergence across features
        # Set self.value to average KL divergence
        self.value = 0

