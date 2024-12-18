import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import numpy as np
from service.newton import NewtonService
from service.differential import DifferentiationService

if __name__ == "__main__":
    service = NewtonService()
    differential = DifferentiationService()
    
    # 方程式とその導関数を定義
    def f(x):
        return x**2 - 10*np.sin(x) - 2
    
    def df(x):
        # return differential.calculate(f, x)
        return 2*x - 10*np.cos(x)
    
    # 初期値，試行回数を設定
    x_initial = 2
    max_iter = 3 

# 実行
solution = service.solve(f, df, x_initial, max_iter)
print(f"指定試行回数後の近似解: {solution}")
