from pydantic import BaseModel
from typing import List

class EigenRequest(BaseModel):
    matrix: List[List[float]]