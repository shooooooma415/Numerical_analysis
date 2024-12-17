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
        matrix = np.array(matrix)  # 行列をNumPy配列に変換
        v = np.array(v).reshape(-1, 1)  # 初期ベクトルを列ベクトルに変換

        while n < max_iter:
            # 行列とベクトルの積を計算
            x = matrix @ v
            r = round(x[0, 0], 2)  # 固有値の推定値を小数第3位で四捨五入
            print(f"反復 {n + 1}  固有値 r: {r}")

            # ベクトルの正規化 (小数第3位で四捨五入)
            v = np.round(x / r, 2)
            print(f"x{n + 1} の値:\n{v}")

            n += 1

        # 最終的な固有値と固有ベクトルを返す
        return r, v
