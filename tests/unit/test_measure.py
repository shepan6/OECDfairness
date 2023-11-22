from math import log2

import deepdiff
import numpy as np
import pandas as pd
import pytest

from ethically import measure
from ethically.models.dataset import Dataset


def test_that_conditional_demographic_disparity_is_computed(create_tmp_file):
    dataset = Dataset(
        **{
            "predictor": "is_nice_person",
            "data": pd.read_csv(create_tmp_file),
        }
    )
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
