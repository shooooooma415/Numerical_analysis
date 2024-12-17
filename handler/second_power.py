import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import numpy as np
from service.second_power import SecondEigenvalueService

def main():
    service = SecondEigenvalueService()

    # 入力行列
    matrix = [
        [4, 1],
        [1, 0]
    ]

    # 反復回数を指定
    max_iter = 3
    
    # 固有値を指定
    eigenvalue = 4
    
    # 固有ベクトルを指定
    eigenvector = [[1],[0.24]]

    second_eigenvalue, matrix_prime = service.calculate(matrix, eigenvalue, eigenvector, max_iter)

    print("\n2番目に大きい固有値:")
    print(second_eigenvalue)

    print("\n最大固有値の影響を取り除いた行列 A':")
    print(matrix_prime)

if __name__ == "__main__":
    main()