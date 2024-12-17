import numpy as np

class EigenService:
    def __init__(self):
        pass

    def calculate(self, matrix):
        """
        行列の固有値と正規化された固有ベクトルを計算する

        Parameters:
        - matrix: 入力行列 (List[List[float]])

        Returns:
        - 固有値 (numpy.ndarray)
        - 正規化された固有ベクトル (numpy.ndarray)
        """
        eigenvalues, eigenvectors = np.linalg.eig(matrix)

        normalized_eigenvectors = []
        for vector in eigenvectors.T:
            norm = np.linalg.norm(vector)
            normalized_vector = vector / norm 
            normalized_eigenvectors.append(normalized_vector)

        normalized_eigenvectors = np.array(normalized_eigenvectors).T
        return eigenvalues, normalized_eigenvectors
