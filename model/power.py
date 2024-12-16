from pydantic import BaseModel
from typing import List

class PowerMethodRequest(BaseModel):
    matrix: List[List[float]]
    v: List[List[float]]
    tolerance: float