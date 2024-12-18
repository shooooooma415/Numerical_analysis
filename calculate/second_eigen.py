import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import numpy as np
from service.second_eigen import SecondEigenService

def main():
    service = SecondEigenService()

    # 行列を入力
    matrix_A = [
        [3, 2],
        [1, 2]
    ]
    # A_dash の計算
    try:
        result = service.eigen(matrix_A)
        print("\n最大固有値の影響を取り除いた行列 A' (Aダッシュ):")
        print(result)

        # 2番目の固有値を計算
        second_eigenvalue = service.eigen_value(result)
        print(f"\n2番目の固有値は: {second_eigenvalue}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()