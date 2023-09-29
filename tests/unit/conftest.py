import pytest
import pandas as pd


def example_data() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {"age": 10, "sex": "male", "is_nice_person": True},
            {"age": 55, "sex": "male", "is_nice_person": False},
            {"age": 42, "sex": "female", "is_nice_person": True},
            {"age": 20, "sex": "female", "is_nice_person": False},
        ]
    )


@pytest.fixture
def create_tmp_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    filename = f"{d}/test_csv.csv"
    example_data().to_csv(filename, index=False)
    return filename
