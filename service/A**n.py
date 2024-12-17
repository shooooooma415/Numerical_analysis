import numpy as np

class MatrixPowerService:
    def __init__(self):
        pass

    def calculate(self, matrix, n):
        """
        行列のn乗を計算する
        Parameters:
        - matrix: 入力行列 (List[List[float]])
        - n: 乗数 (int)

        Returns:
        - n乗した行列 (numpy.ndarray)
        """
        return np.linalg.matrix_power(matrix, n)
