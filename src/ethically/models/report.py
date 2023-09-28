from pydantic import BaseModel

class Report(BaseModel):
    kind: str

class EthicsReport:
    kind: Literal["ethics"] = "ethics"