import numpy as np

class PowerMethodService:
    def __init__(self):
        pass

    def calculate(self, matrix, v, max_iter=100):
        """
        冪乗法で最大固有値と対応する固有ベクトルを計算する

        Parameters:
        - matrix: 入力行列 (List[List[float]])
        - v: 初期ベクトル (List[List[float]])
        - max_iter: 最大反復回数 (int)

        Returns:
        - 固有値 (float): 最大固有値
        - 固有ベクトル (numpy.ndarray): 正規化された固有ベクトル
        """
        n = 0
        matrix = np.array(matrix)
        v = np.array(v).reshape(-1, 1)

        while n < max_iter:
            x = matrix @ v
            r = round(x[0, 0], 2)
            print(f"反復 {n + 1}  固有値 r: {r}")

            v = np.round(x / r, 2)
            print(f"x{n + 1} の値:\n{v}")

            n += 1
        return r, v
