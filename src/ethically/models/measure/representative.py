from ethically.models.measure import Metric
from typing import Literal

class RepresentativeMetric(Metric):
    kind: Literal["representativeness"] = "representativeness"

class DatasetDivergenceMetric(RepresentativeMetric):
    name: Literal["dataset-divergence"] = "dataset-divergence"
    
    # def _compute():
    #     pass