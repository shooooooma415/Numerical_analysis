import numpy as np

class RayleighService:
    def __init__(self):
        pass

    def calculate(self, matrix, x, limit):
        """
        レイリー商を用いて最大固有値を求める
        """
        while True:
            x_d = matrix @ x
            r = (x @ x_d) / (x @ x)
            x_d = x_d / np.linalg.norm(x_d)
            if abs(r - limit) < 1e-5:
                return r
            x = x_d
