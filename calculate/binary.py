import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from service.binary import BinarySearchService

# 対象関数を定義
def f(x):
    return x**2 - 2

if __name__ == "__main__":
    service = BinarySearchService()

    a = 1  # 区間の下限
    b = 2  # 区間の上限
    tolerance = 0.3  # 許容誤差
    max_iter = 50  # 最大反復回数

    try:
        solution, iterations = service.search(f, a, b, tolerance, max_iter)
        print(f"\n近似解: {solution}")
        print(f"試行回数: {iterations}")
    except ValueError as e:
        print(f"エラー: {e}")
