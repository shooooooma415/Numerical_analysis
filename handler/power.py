import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import numpy as np
from service.power import PowerMethodService

import ast

def main():
    # PowerMethodServiceのインスタンスを作成
    service = PowerMethodService()

    matrix = [
        [4, 1],
        [1, 0]
    ]
    
    initial_vector = [[1], [0]]

    # 反復回数と収束判定値の入力
    max_iter = 4

    eigenvalue, eigenvector = service.calculate(matrix, initial_vector, max_iter)

    # 結果の表示
    if eigenvalue is not None:
        print("\n最大固有値:")
        print(eigenvalue)
        print("\n対応する正規化固有ベクトル:")
        print(eigenvector)
    else:
        print("収束しませんでした。")

if __name__ == "__main__":
    main()
