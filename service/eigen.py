# 固有値と固有ベクトル
import ast
import numpy as np

def eigen(A):
    eigenvalues, eigenvectors = np.linalg.eig(A)
    
    diagonal_matrix = np.diag(eigenvalues)

    print("固有値")
    print(eigenvalues)
    print("固有値からなる対角行列:")
    print(diagonal_matrix)
    
    print("固有ベクトル:")
    print(eigenvectors)
# 二次元配列で入力
print("対象となる行列を入力:")
matrix_A_input = input() 
matrix_A = np.array(ast.literal_eval(matrix_A_input))
eigen(matrix_A)
