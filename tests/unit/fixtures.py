import pytest
import pandas as pd

def example_df() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "age": 10,
                "sex": "male",
                "nice_person": True
            },
            {
                "age": 55,
                "sex": "male",
                "nice_person": False
            },
            {
                "age": 42,
                "sex": "female",
                "nice_person": True
            },
            {
                "age": 20,
                "sex": "female",
                "nice_person": False
            }
        ]
    )

def create_tmp_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    example_df().to_csv("{d}/test_csv.csv")



