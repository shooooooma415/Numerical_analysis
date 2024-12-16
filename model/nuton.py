from pydantic import BaseModel
from typing import List

class NewtonRequest(BaseModel):
    x: float
    accuracy: float