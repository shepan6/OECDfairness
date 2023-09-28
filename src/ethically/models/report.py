from pydantic import BaseModel
from typing import Literal

class Report(BaseModel):
    kind: str

class EthicsReport:
    kind: Literal["ethics"] = "ethics"