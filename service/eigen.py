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
        # 固有値と固有ベクトルを計算
        eigenvalues, eigenvectors = np.linalg.eig(matrix)

        # 固有ベクトルを正規化（各列ベクトルをノルム1にする）
        normalized_eigenvectors = []
        for vector in eigenvectors.T:  # 固有ベクトルは列ベクトルとして格納されている
            norm = np.linalg.norm(vector)  # ベクトルのノルムを計算
            normalized_vector = vector / norm  # 正規化
            normalized_eigenvectors.append(normalized_vector)

        # 正規化された固有ベクトルを2次元配列に戻す
        normalized_eigenvectors = np.array(normalized_eigenvectors).T
        return eigenvalues, normalized_eigenvectors
