import pandas as pd
import pytest

from ethically.models.dataset import Dataset

def example_data() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {"age": 10, "sex": "male", "is_nice_person": True},
            {"age": 55, "sex": "male", "is_nice_person": False},
            {"age": 42, "sex": "female", "is_nice_person": True},
            {"age": 20, "sex": "female", "is_nice_person": True},
        ]
    )


@pytest.fixture
def create_tmp_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    filename = f"{d}/test_csv.csv"
    example_data().to_csv(filename, index=False)
    return filename

@pytest.fixture
def example_dataset(create_tmp_file):
    dataset = Dataset(
        **{
            "predictor": "is_nice_person",
            "data": pd.read_csv(create_tmp_file),
        }
    )
    return dataset