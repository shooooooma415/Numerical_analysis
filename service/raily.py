import numpy as np

class RayleighService:
    def __init__(self):
        pass

    def calculate(self, matrix, x, max_iter=100, tolerance=1e-5):
        """
        冪乗法を用いてレイリー商で最大固有値を計算する
        反復ごとに固有値も表示する
        """
        x = x / np.linalg.norm(x)

        for i in range(max_iter):
            x_d = matrix @ x
            
            r = (x @ x_d) / (x @ x)
            
            x_d = x_d / np.linalg.norm(x_d)
            
            print(f"反復 {i + 1}: 固有値 r: {r}")
            
            if np.abs(r - (x @ x_d) / (x @ x)) < tolerance:
                print(f"収束した！反復回数: {i+1}")
                break

            x = x_d

        return round(r, 6), x_d
