import logging
from typing import Any, Literal, Union
from math import sqrt

from collections import Counter
import numpy as np
from pydantic import BaseModel, Field, RootModel, TypeAdapter, Discriminator, Tag
from pydantic.types import PositiveInt
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import KFold
from typing import Annotated

from ethically.models.dataset import Dataset
from ethically.models.exceptions import (
    FeatureNotInDataset,
    FeatureSubCategoryNotInDataset,
)


class BaseMetric(BaseModel):
    name: str = Field(...)
    objective: str
    lifecycle_stages: list[str]
    purpose: list[str]
    risk_management_stage: list[str]
    value: float = float("-inf")  # Default value that we can filter out by

    def _compute(self, dataset: Dataset = None) -> None:
        raise NotImplementedError(
            """You have hit the base model method. The model requires a _compute() method"""
        )


class ConditionalDemographicDisparity(BaseMetric):
    name: Literal[
        "conditional-demographic-disparity"
    ] = "conditional-demographic-disparity"
    objective: str = "fairness"
    lifecycle_stages: list[str] = [
        "Verify & validate",
        "Build & interpret model",
        "Plan & design",
    ]
    purpose: list[str] = ["Reasoning with knowledge structures/planning"]
    risk_management_stage: list[str] = ["Define"]
    feature: str
    disadvantaged: str

    def _compute(self, dataset: Dataset = None) -> None:
        # Applied to each feature
        logging.info("Computing diverse-uniformity Divergence...")
        data = dataset.data

        if self.feature not in data.columns:
            raise FeatureNotInDataset()
        unique_feature_values = data.loc[:, self.feature].unique()
        if self.disadvantaged not in unique_feature_values:
            raise FeatureSubCategoryNotInDataset()

        data[dataset.predictor] = data[dataset.predictor].astype(int)
        mapping = self._generate_disadvantaged_mapping(
            unique_feature_values=unique_feature_values
        )
        data["disadvantaged"] = data.loc[:, self.feature].map(mapping)
        grouped = data.groupby(["disadvantaged", dataset.predictor]).count()
        grouped /= grouped.groupby(level=1).sum()
        grouped.reset_index(inplace=True)

        probs = grouped[grouped["disadvantaged"] == 1].iloc[:, -1].values

        if len(probs) == 1:
            multiplier = (
                grouped[grouped["disadvantaged"] == 1][
                    dataset.predictor
                ].values
                * -1
            )
            probs *= multiplier
            value = probs[0]
        else:
            value = np.diff(probs)[0]

        self.value = float(value)

    def _generate_disadvantaged_mapping(
        self, unique_feature_values=[]
    ) -> dict[str, int]:
        mapping: dict[str, int] = {}
        for k in unique_feature_values:
            if k == self.disadvantaged:
                v = 1
            else:
                v = 0
            mapping[k] = v

        return mapping

class HellingerDistance(BaseMetric):
    name: Literal["hellinger-distance"] = "hellinger-distance"
    objective: str = "fairness"
    lifecycle_stages: list[str] = [
        "Operate & monitor",
        "Verify & validate",
        "Build & interpret model"
    ]
    purpose: list[str] = [
        "Event/anomaly detection"
        "Forecasting/prediction",
        "Reasoning with knowledge structures/planning",
        "Recognition/object detection",
    ]
    risk_management_stage: list[str] = [
        "Define",
        "Assess",
        "Govern",
        "Treat"
    ]
    feature: str
    comparison_dataset: Dataset

    def _compute(self, dataset: Dataset = None) -> None:
        # Applied to each feature
        logging.info("Computing diverse-uniformity Divergence...")
        data = dataset.data

        feature_counts = {}

        feature_counts["dataset"] =  self._compute_square_root_probs(Counter(dataset.data.loc[:, self.feature].values))
        feature_counts["comparison_dataset"] =  self._compute_square_root_probs(Counter(self.comparison_dataset.data.loc[:, self.feature].values))
        
        distance: float = 0.0
        for f in feature_counts["dataset"]:
            distance += (feature_counts["dataset"][f] - feature_counts["dataset"][f])
        
        distance = 1/sqrt(2)*sqrt(distance)
        print(distance)
        self.value = distance

    @staticmethod
    def _compute_square_root_probs(counts: Counter) -> dict[str, float]:
        
        count_sum: PositiveInt = counts.total()
        counts: dict[str, float] = dict(counts)
        for key in counts.keys():
            counts[key] = sqrt(counts[key]/count_sum)

        return counts

# # TODO: Resolve typing.Union Error from adding HellingerDistance to Union
# https://docs.pydantic.dev/latest/concepts/unions/#discriminated-unions
# Do I have to store the discrimation union in a class
# Metric = Annotated[
#     Union[HellingerDistance, ConditionalDemographicDisparity],
#     Field(discriminator='name')
# ]


def get_discriminator_value(v: Any) -> str:
    return v.get('name')

class Metric(BaseModel):
    metric: Annotated[
        Union[
            Annotated[HellingerDistance, Tag('hellinger-distance')],
            Annotated[ConditionalDemographicDisparity, Tag('conditional-demographic-disparity')],
        ],
        Discriminator(get_discriminator_value),
    ]

ALL_METRICS = Union[HellingerDistance, ConditionalDemographicDisparity]

Metric = Annotated[ALL_METRICS, Field(discriminator="name")]
# NOTE: solution taken from https://github.com/pydantic/pydantic/discussions/4950#discussioncomment-6462134
metric_adapter: TypeAdapter[ALL_METRICS] = TypeAdapter(Metric)

class Metrics(RootModel):
    root: list[Metric] = []

    def compute_all(
        self, data: Any, metric_payloads: list[dict] = []
    ) -> Metric:
        for metric_payload in metric_payloads:
            metric: Metric = Metric.parse_object(metric_payload)
            metric._compute(data=data)
            return metric

    def append(self, metric: Metric):
        self.root.append(metric)

    def __len__(self) -> int:
        return len(self.root)

    def __getitem__(self, key):
        return self.root[key]


# class RepresentativeMetric(BaseMetric):
#     kind: Literal["representativeness"] = "representativeness"


# class DiverseUniformityMetric(RepresentativeMetric):
#     name: Literal["diverse-uniformity-divergence"] = "diverse-uniformity-divergence"

#     def _compute(self, data: Any = None):
#         # Applied to each feature
#         logging.info("Computing diverse-uniformity Divergence...")
#         print("DATA: ", data)

#         diversity: float = self._compute_diversity(data=data)
#         exclusion: float = self._compute_exclusion(data=data)

#         return diversity * exclusion

#     def _compute_diversity(data: Any = None):

#         c = data.groupby().count()
#         c /= c.sum()
#         # apply log(1/probability)
#         # negative sum

#     def _compute_exclusion(data: Any = None):

#         # compute Gini index


# class CrossEntropyDivergenceMetric(RepresentativeMetric):
#     name: Literal["cross-entropy-divergence"] = "cross-entropy-divergence"

#     def _compute(self, data: Any = None):
#         logging.info("Computing Cross Entropy Divergence...")
#         print("DATA: ", data)
#         coefficients = np.array(
#             [np.linspace(1, 0, len(data)+1),
#             np.linspace(0, 1, len(data)+1)]
#         ).T
#         feature_level_count = data.groupby(self.features).count()
#         true_dist = feature_level_count / feature_level_count.sum()
#         log_true_dist = np.log2(true_dist.iloc[:, 0].values).reshape((-1, 1))


#         self.value = np.mean(np.dot(coefficients, log_true_dist) * -1)
#         print(self.value)
#         print(coefficients)


# class DatasetDivergenceMetric(RepresentativeMetric):
#     name: Literal["dataset-divergence"] = "dataset-divergence"

#     def _compute(self, data: Any = None, features: list[str] = []):
#         logging.info("Computing Dataset Divergence...")
#         print("DATA: ", data)
#         if features:
#             # subset features first
#             pass
#         # Split data into train/test
#         kf = KFold(n_splits=3, shuffle=True)
#         for i, (train_index, test_index) in enumerate(kf.split(data)):
#             X_train = data.iloc[train_index, :]
#             X_test = data.iloc[test_index, :]
#             # Compute KL divergence across features
#             print(X_train)
#             print(X_test)
#             # Set self.value to average KL divergence
#         self.value = 0
