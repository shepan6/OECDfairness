import pytest
import pandas as pd
import numpy as np
from math import log2
from ethically.models.dataset import Dataset

@pytest.mark.skip(reason="temporarily deprecated")
def test_that_datasets_cross_entropy_representativeness_is_measured(create_tmp_file):
    dataset = Dataset(
        **{"predictor": ["is_nice_person"], "data": pd.read_csv(create_tmp_file)}
    )
    dataset.measure(metric_names=["cross-entropy-divergence"], features=["sex"])
    assert len(dataset.measures) == 1
    ce_coefficients = np.array(
        [
            [0.5, 1.5],
            [0.25, 1.25],
            [0.5,0.5],
            [1.25, 0.25],
            [1.5, 0.5]
        ]
    )
    ce_logs = np.array(
        [[log2(0.5)], [log2(0.5)]]
    )
    ce_value = np.mean(np.dot(ce_coefficients, ce_logs) * -1)
    assert dataset.measures[0].model_dump() == {
        "name": "dataset-divergence",
        "kind": "representativeness",
        "features": ["sex"],
        "value": ce_value,
    }

@pytest.mark.skip(reason="Not yet Implemented")
def test_that_datasets_representativeness_is_measured(create_tmp_file):
    dataset = Dataset(
        **{"predictor": ["is_nice_person"], "data": pd.read_csv(create_tmp_file)}
    )
    dataset.measure(metric_names=["dataset-divergence"])
    assert len(dataset.measures) == 1
    assert dataset.measures[0].model_dump() == {
        "name": "dataset-divergence",
        "kind": "representativeness",
        "value": 1,
    }
