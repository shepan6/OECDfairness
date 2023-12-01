from math import log2, sqrt

import deepdiff
import numpy as np
import pandas as pd
import pytest

from ethically import measure
from ethically.models.dataset import Dataset
from ethically.models.exceptions import (
    FeatureNotInDataset,
    FeatureSubCategoryNotInDataset,
)


def test_that_conditional_demographic_disparity_is_computed(example_dataset):
    dataset = example_dataset
    metric: dict = {
        "name": "conditional-demographic-disparity",
        "feature": "sex",
        "disadvantaged": "female",
    }
    result = measure(dataset=dataset, metrics=[metric])
    assert len(result) == 1
    diff = deepdiff.DeepDiff(
        result[0].model_dump(),
        {
            **metric,
            "objective": "fairness",
            "lifecycle_stages": [
                "Verify & validate",
                "Build & interpret model",
                "Plan & design",
            ],
            "purpose": ["Reasoning with knowledge structures/planning"],
            "risk_management_stage": ["Define"],
            "value": -2 / 3,  # 0/1 - 2/3
        },
    )
    assert not diff


@pytest.mark.parametrize(
    "metric_payload,expected_exception",
    [
        pytest.param(
            {
                "name": "conditional-demographic-disparity",
                "feature": "not-in-data",
                "disadvantaged": "female",
            },
            FeatureNotInDataset,
            id="feature-not-in-dataset",
        ),
        pytest.param(
            {
                "name": "conditional-demographic-disparity",
                "feature": "sex",
                "disadvantaged": "not-in-data",
            },
            FeatureSubCategoryNotInDataset,
            id="feature-subcategory-not-in-dataset",
        ),
    ],
)
def test_that_conditional_demographic_disparity_throws_exceptions(
    example_dataset, metric_payload, expected_exception
):
    dataset = example_dataset

    with pytest.raises(expected_exception) as e_info:
        measure(dataset=dataset, metrics=[metric_payload])


def test_that_hellinger_distance_is_computed(example_dataset):
    dataset = example_dataset
    metric: dict = {
        "name": "hellinger-distance",
        "feature": "sex",
        "comparison_dataset": Dataset(
            data=pd.DataFrame([
                {"sex": "male", "pred": 0},
                {"sex": "female", "pred": 1},
                {"sex": "female", "pred": 0}
            ]),
            predictor="pred"
        )
    }
    result = measure(dataset=dataset, metrics=[metric])
    print(result)
    assert len(result) == 1
    diff = deepdiff.DeepDiff(
        result[0].model_dump(),
        {
            **metric,
            "objective": "fairness",
            "lifecycle_stages": [
                "Operate & monitor",
                "Verify & validate",
                "Build & interpret model"
            ],
            "purpose": [
                "Event/anomaly detection"
                "Forecasting/prediction",
                "Reasoning with knowledge structures/planning",
                "Recognition/object detection",
            ],
            "risk_management_stage": [
                "Define",
                "Assess",
                "Govern",
                "Treat"
            ],
            "value": (1/sqrt(2))*(sqrt((sqrt(0.5) - sqrt(1/3))**2 + (sqrt(0.5) - sqrt(2/3))**2)),
        },
    )
    assert not diff