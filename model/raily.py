from pydantic import BaseModel
from typing import List

class RayleighRequest(BaseModel):
    matrix: List[List[float]]
    x: List[float]
    limit: float