import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import numpy as np
from service.eigen import EigenService

def main():
    service = EigenService()

    # 入力行列を指定
    matrix = [
        [4, 1],
        [1, 0]
    ]

    eigenvalues, eigenvectors = service.calculate(np.array(matrix))

    print("固有値:")
    print(eigenvalues)
    print("\n固有ベクトル:")
    print(eigenvectors)

if __name__ == "__main__":
    main()
