import pytest
from ethically import Dataset

@pytest.mark.parametrize(
    "args",
    [
        pytest.param(
            {
                "filepath": "temp/file/path",
                "predictor": ["predictor"]
            },
            id="from_filepath"
        )
    ]
)
def test_that_dataset_is_loaded(args: dict) -> None:
    
    dataset = Dataset(**args)
    assert len(dataset.raw) > 0

def test_that_dataset_loading_raises_exceptions():
    pass

