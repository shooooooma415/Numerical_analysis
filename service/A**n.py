# A^n行列
import ast
import numpy as np

def a_n(matrix, n):
    return np.linalg.matrix_power(matrix, n)
# ここにn乗したい行列
# 二次元配列で入力
print("対象となる行列を入力:")
matrix_A_input = input() 
matrix_A = np.array(ast.literal_eval(matrix_A_input))
n =int(input("乗数:"))
result = a_n(matrix_A, n)

print(f"Aの{n}乗:")
print(result)
