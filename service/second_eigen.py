import numpy as np

class SecondEigenService:
    def __init__(self):
        pass

    def eigen(self, A):
        """
        最大固有値の影響を取り除いた行列を計算する
        Parameters:
        - A: 入力行列 (numpy.ndarray)

        Returns:
        - A_dash: 最大固有値の影響を取り除いた行列 (numpy.ndarray)
        """
        eigenvalues, eigenvectors = np.linalg.eig(A)
        sorted_pairs = sorted(zip(eigenvalues, eigenvectors.T), key=lambda x: x[0], reverse=True)
        max_eigenvalue, max_eigenvector = sorted_pairs[0]
        
        max_eigenvector_transposed = np.array(max_eigenvector).reshape(-1, 1)
        A_dash = A - max_eigenvalue * np.dot(max_eigenvector_transposed, max_eigenvector_transposed.T)
        return A_dash

    def eigen_value(self, A_dash):
        """
        A_dash の最大固有値を計算する (2番目の固有値)
        Parameters:
        - A_dash: 最大固有値の影響を取り除いた行列 (numpy.ndarray)

        Returns:
        - max_eigenvalue: A_dash の最大固有値 (float)
        """
        eigenvalues, _ = np.linalg.eig(A_dash)
        return round(max(eigenvalues),2)
