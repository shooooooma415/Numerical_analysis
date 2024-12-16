# 冪乗で固有値計算
import ast
import numpy as np

def power(matrix, v, limit=0.001, max_iter=100):
    n = 0
    while n < max_iter:
        x = matrix @ v 
        r = x[0,0]
        print(f"反復 {n + 1}  固有値r: {r}")
        v = x / r 
        n += 1
        print("x{}の値は\n{}".format(n,v))
        if np.linalg.norm(matrix @ v - r * v) < limit:
            print("収束した！")
            return r, v   
    return None
# 対象の行列
# 二次元配列で入力
print("対象となる行列を入力:")
matrix_A_input = input() 
matrix_A = np.array(ast.literal_eval(matrix_A_input))

# 初期値  
print("v_0を入力:")
initialmat_input = input()
initialmat = np.array(ast.literal_eval(initialmat_input))
power(matrix_A, initialmat)
