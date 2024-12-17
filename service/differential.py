import sympy as sp

class DifferentiationService:
    def __init__(self):
        pass

    def calculate(self, func, var):
        """
        シンボリック微分を計算する（sympyライブラリを使用）

        Parameters:
        - func: 微分する関数 (sympy式)
        - var: 微分対象の変数 (sympy.Symbol)

        Returns:
        - f'(x): シンボリック微分の結果 (sympy式)
        """
        return sp.diff(func, var)
