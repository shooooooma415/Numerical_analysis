from pydantic import BaseModel
from typing import List

class BinarySearchRequest(BaseModel):
    a: float
    b: float
    tolerance: float