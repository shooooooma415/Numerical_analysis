import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from service.matrix_power import MatrixPowerService
import numpy as np

def main():
    service = MatrixPowerService()

    # 入力行列と乗数を指定
    matrix = [
        [1, 2],
        [3, 4]
    ]
    n = 3  # 乗数

    # 実行
    print("入力行列:")
    print(np.array(matrix))
    print(f"乗数: {n}")

    try:
        result = service.calculate(matrix, n)
        print(f"\n行列の {n} 乗:")
        print(result)
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()
