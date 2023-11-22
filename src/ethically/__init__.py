import logging

from ethically.models.dataset import Dataset
from ethically.models.measure.metric import Metric, Metrics


def measure(dataset: Dataset, metrics: list[dict]) -> Metrics:
    new_metrics: Metrics = Metrics()

    for metric_payload in metrics:
        metric: Metric = Metric(**metric_payload)
        metric._compute(dataset=dataset)
        new_metrics.append(metric)

    return new_metrics
