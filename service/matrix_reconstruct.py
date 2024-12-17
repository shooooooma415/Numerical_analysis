import numpy as np

class MatrixReconstructionService:
    def __init__(self):
        pass

    def reconstruct(self, eigenvalues, eigenvectors):
        """
        固有値と固有ベクトルから行列を再構築する
        
        Parameters:
        - eigenvalues: 固有値のリストまたは配列 (List[float])
        - eigenvectors: 固有ベクトルを列ベクトルとする行列 (numpy.ndarray)

        Returns:
        - 再構築された行列 (numpy.ndarray)
        """
        lambda_matrix = np.diag(eigenvalues)
        
        V = eigenvectors

        reconstructed_matrix = V @ lambda_matrix @ V.T
        return reconstructed_matrix
