import pytest
import pandas as pd
from ethically.models.dataset import Dataset


def test_that_datasets_representativeness_is_measured(create_tmp_file):
    dataset = Dataset(
        **{"predictor": ["is_nice_person"], "data": pd.read_csv(create_tmp_file)}
    )
    dataset.measure(metric_names=["dataset-divergence"])
    print(dataset.measures)
    assert len(dataset.measures) == 1
    assert dataset.measures[0].model_dump() == {
        "name": "dataset-divergence",
        "kind": "representativeness",
        "value": 1,
    }
