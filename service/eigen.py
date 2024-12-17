import numpy as np

class EigenService:
    def __init__(self):
        pass

    def calculate(self, matrix):
        """
        行列の固有値と固有ベクトルを計算する
        Parameters:
        - matrix: 入力行列 (List[List[float]])

        Returns:
        - 固有値 (numpy.ndarray)
        - 固有ベクトル (numpy.ndarray)
        """
        eigenvalues, eigenvectors = np.linalg.eig(matrix)
        return eigenvalues, eigenvectors
