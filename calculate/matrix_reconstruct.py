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

    service = MatrixReconstructionService()

    reconstructed_matrix = service.reconstruct(eigenvalues, eigenvectors)

    print(f"再構築された行列:\n{reconstructed_matrix}")

if __name__ == "__main__":
    main()
