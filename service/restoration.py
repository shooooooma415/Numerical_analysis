# AVV^t = V /\_ V^T
import numpy as np
def restration(A, V):
    return V @ A @ V.T


# 固有値の対角要素
A = np.diag([5, 3])
print("固有値の対角要素は\n{}".format(A))
# 固有ベクトル
V = np.array([[1/np.sqrt(2), 1/np.sqrt(2)],[-1/np.sqrt(2), 1/np.sqrt(2)]])
print(V)
print("固有ベクトルは\n{}".format(V))
print("復元結果は\n{}".format(restration(A,V)))
