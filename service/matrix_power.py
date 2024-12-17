# A^n行列
import numpy as np

class MatrixPowerService():
    def __init__(self) -> None:
        pass
    
    def calculate(self,matrix, n):
        return np.linalg.matrix_power(matrix, n)

