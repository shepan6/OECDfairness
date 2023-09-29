import pytest
import pandas as pd
from ethically.models.dataset import Dataset


def test_that_datasets_representativeness_is_measured(create_tmp_file):
    dataset = Dataset(
        **{"predictor": ["is_nice_person"], "data": pd.read_csv(create_tmp_file)}
    )
    dataset.measure(["dataset-divergence"])
    assert len(dataset.measures) == 1
    assert dataset.measures[0].dict == {
        "name": "dataset-divergence",
        "kind": "representativeness",
        "value": 1,
    }
