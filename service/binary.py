import numpy as np

class BinarySearchService:
    def __init__(self):
        # 初期化が必要であればここに記述
        pass

    def f(self, x):
        """対象となる関数"""
        return x**2 - 10 * np.sin(x) - 2

    def search(self, a, b, tolerance, max_iter=50):
        """
        二分法を用いて解を探索する
        
        Parameters:
        - a: 区間の下限
        - b: 区間の上限
        - tolerance: 許容誤差
        - max_iter: 最大反復回数（デフォルト50）

        Returns:
        - 解 (float)
        """
        if self.f(a) * self.f(b) > 0:
            raise ValueError("f(a) と f(b) の符号が同じです")

        for _ in range(max_iter):
            c = (a + b) / 2.0
            if abs(b - a) < tolerance:
                return c
            if self.f(c) * self.f(a) < 0:
                b = c
            else:
                a = c
        return (a + b) / 2.0
