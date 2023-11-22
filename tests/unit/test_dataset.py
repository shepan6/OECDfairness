import pandas as pd
import pytest

from ethically.models.dataset import Dataset


@pytest.mark.parametrize(
    "args",
    [
        pytest.param(
            {"predictor": "is_nice_person"}, id="from_pandas.DataFrame"
        )
    ],
)
def test_that_dataset_is_loaded(create_tmp_file, args: dict) -> None:
    args["data"] = pd.read_csv(create_tmp_file)
    dataset = Dataset(**args)
    assert dataset.data is not None


def test_that_dataset_loading_raises_exceptions():
    pass


# Add functionality to find most representative dataset from divergence metric
