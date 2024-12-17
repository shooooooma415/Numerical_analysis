import numpy as np
from service.newton import NewtonService

if __name__ == "__main__":
    # ニュートンサービスのインスタンスを作成
    service = NewtonService()
    
    # 方程式とその導関数を定義
    def f(x):
        return x**2 - 2
    
    def df(x):
        return 2 * x
    
    # 初期値や条件を設定
    x_initial = 2
    max_iter = 5     # 試行回数

# 実行
solution = service.solve(f, df, x_initial, max_iter)
print(f"指定試行回数後の近似解: {solution}")
