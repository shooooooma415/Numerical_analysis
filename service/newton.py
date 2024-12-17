class NewtonService:
    def __init__(self):
        pass

    def solve(self, f, df, x, max_iter):
        """
        ニュートン法で方程式の解を求める（試行回数を指定）

        Parameters:
        - f: 方程式の対象関数 (callable)
        - df: 対象関数の導関数 (callable)
        - x: 初期値 (float)
        - max_iter: 実行する試行回数 (int)

        Returns:
        - 解 (float): 指定回数実行後の近似解
        """
        for iteration in range(1, max_iter + 1):
            x = round(x - f(x) / df(x), 2)  # xを小数第3位で四捨五入
            f_value = round(f(x), 2)       # f(x)も小数第3位で四捨五入
            print(f"試行回数: {iteration}, x: {x}")
        return x
