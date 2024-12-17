import numpy as np

class RayleighService:
    def __init__(self):
        pass

    def calculate(self, matrix, x, max_iter=100, tolerance=1e-5):
        """
        冪乗法を用いてレイリー商で最大固有値を計算する
        反復ごとに固有値も表示する
        """
        # 初期ベクトルの正規化
        x = x / np.linalg.norm(x)

        for i in range(max_iter):
            # 行列とベクトルの積を計算
            x_d = matrix @ x
            
            # レイリー商 (固有値の推定)
            r = (x @ x_d) / (x @ x)
            
            # ベクトルの正規化
            x_d = x_d / np.linalg.norm(x_d)
            
            # 反復中の固有値を表示
            print(f"反復 {i + 1}: 固有値 r: {r}")
            
            # 収束判定
            if np.abs(r - (x @ x_d) / (x @ x)) < tolerance:
                print(f"収束した！反復回数: {i+1}")
                break

            # 次の反復用にベクトルを更新
            x = x_d

        return round(r, 6), x_d
