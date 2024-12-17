import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import numpy as np
from service.raily import RayleighService

def main():
    service = RayleighService()
    # サンプル行列
    matrix = np.array([[4, 1], [2, 3]])

    # 初期ベクトル
    x = np.array([1, 1])

    # 反復回数
    max_iter = 3
    

    # 最大固有値と対応する固有ベクトルを求める
    max_eigenvalue, eigenvector = service.calculate(matrix, x, max_iter)

    # 結果の表示
    print(f"最大固有値: {max_eigenvalue}")
    print(f"対応する固有ベクトル:\n{eigenvector}")
    
if __name__ == "__main__":
    main()