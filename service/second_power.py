import numpy as np

class SecondEigenvalueService:
    def __init__(self):
        pass

    def calculate(self, matrix, eigenvalue, eigenvector, max_iter=100):
        """
        ユーザー指定の固有値と固有ベクトルを使い、行列からその影響を取り除いた行列を計算し、
        2番目に大きい固有値を冪乗法で求める
        
        Parameters:
        - matrix: 入力行列 (numpy.ndarray)
        - eigenvalue: 最大固有値 (float)
        - eigenvector: 最大固有ベクトル (numpy.ndarray)
        - max_iter: 最大反復回数 (int)

        Returns:
        - second_eigenvalue: 2番目の固有値 (float)
        - matrix_prime: 最大固有値の影響を取り除いた行列 A' (numpy.ndarray)
        """
        matrix = np.array(matrix)
        eigenvector = np.array(eigenvector).reshape(-1, 1)

        eigenvector_normalized = eigenvector / np.linalg.norm(eigenvector)
        matrix_prime = matrix - eigenvalue * (eigenvector_normalized @ eigenvector_normalized.T)
        matrix_prime = np.round(matrix_prime, 2)

        print(f"最大固有値の影響を取り除いた行列 A':\n{matrix_prime}")

        second_eigenvalue, _ = self.power_method(matrix_prime, eigenvector, max_iter)
        second_eigenvalue = round(second_eigenvalue, 2)

        print(f"\n2番目に大きい固有値: {second_eigenvalue}")
        return second_eigenvalue, matrix_prime

    def power_method(self, matrix, v, max_iter=100):
        """
        冪乗法で最大固有値と対応する固有ベクトルを求める

        Parameters:
        - matrix: 入力行列 (numpy.ndarray)
        - v: 初期ベクトル (numpy.ndarray)
        - max_iter: 最大反復回数 (int)

        Returns:
        - 固有値 (float)
        - 固有ベクトル (numpy.ndarray)
        """
        for i in range(max_iter):
            x = matrix @ v 
            eigenvalue = round(x[0, 0], 2) 
            v = np.round(x / eigenvalue, 2)

            print(f"\n反復 {i + 1}: 固有値 r: {eigenvalue}")
            print(f"対応する固有ベクトル:\n{v}")

        return eigenvalue, v
