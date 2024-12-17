import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import numpy as np
from service.matrix_reconstruct import MatrixReconstructionService

def main():
    # 固有値と固有ベクトル
    eigenvalues = [5, 3]
    eigenvectors = np.array([[1/np.sqrt(2), 1/np.sqrt(2)],
                            [-1/np.sqrt(2), 1/np.sqrt(2)]])

    # MatrixReconstructionServiceのインスタンス作成
    service = MatrixReconstructionService()

    # 固有値と固有ベクトルから行列を再構築
    reconstructed_matrix = service.reconstruct(eigenvalues, eigenvectors)

    # 結果の表示
    print(f"再構築された行列:\n{reconstructed_matrix}")

if __name__ == "__main__":
    main()
