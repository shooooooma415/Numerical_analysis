from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import ast
from typing import List, Union

app = FastAPI()

class MatrixInput(BaseModel):
    matrix: List[List[float]]
    n: Union[int, None] = None  # 任意で乗数指定

@app.post("/matrix_power")
def calculate_matrix_power(data: MatrixInput):
    try:
        matrix = np.array(data.matrix)
        if data.n is None:
            return {"error": "乗数 (n) を指定してください"}
        result = np.linalg.matrix_power(matrix, data.n)
        return {"result": result.tolist()}
    except Exception as e:
        return {"error": str(e)}

class EigenInput(BaseModel):
    matrix: List[List[float]]

@app.post("/eigen")
def calculate_eigen(data: EigenInput):
    try:
        matrix = np.array(data.matrix)
        eigenvalues, eigenvectors = np.linalg.eig(matrix)
        return {
            "eigenvalues": eigenvalues.tolist(),
            "eigenvectors": eigenvectors.tolist()
        }
    except Exception as e:
        return {"error": str(e)}

# 他のアルゴリズムも同様に関数化して追加
