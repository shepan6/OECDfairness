from pydantic import BaseModel
from typing import Literal


class Metric(BaseModel):
    kind: str
    name: str
    value: float = float('-inf') # Default value that we can filter out by

    def _compute(self):
        raise NotImplementedError("You have hit the base model method. The model requires a _compute() method")
