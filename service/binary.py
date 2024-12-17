class BinarySearchService:
    def __init__(self):
        pass

    def search(self, f, a, b, tolerance, max_iter=50):
        """
        二分法を用いて解を探索する (小数第3位で四捨五入)

        Parameters:
        - f: 対象の関数 (callable)
        - a: 区間の下限 (float)
        - b: 区間の上限 (float)
        - tolerance: 許容誤差 (float)
        - max_iter: 最大反復回数 (int, デフォルト50)

        Returns:
        - 解 (float): 近似解
        - 試行回数 (int)
        
        Raises:
        - ValueError: f(a) と f(b) の符号が同じ場合
        """
        if f(a) * f(b) > 0:
            raise ValueError("f(a) と f(b) の符号が同じです")

        iteration = 0

        for iteration in range(1, max_iter + 1):
            c = round((a + b) / 2.0, 2)
            print(f"試行回数: {iteration}, a: {round(a, 3)}, b: {round(b, 2)}, c: {c}")

            if round(abs(b - a), 2) < tolerance:
                return c, iteration

            if f(c) * f(a) < 0:
                b = c
            else:
                a = c

        return round((a + b) / 2.0, 2), iteration
