# レイリー商
# 最大固有値を求めたい
import numpy as np
def reily(A, x, limit = 5.00):
        x_d = A @ x
        print("x_dは\n{}".format(x_d))
        r = (np.array(x) @ x_d)/(np.array(x) @ x)
        print("レイリー商は\n{}".format(r))
        abs_x_d = np.sqrt(x_d[0]** 2 + x_d[1] ** 2)
        x_d = [x_d[0] / abs_x_d, x_d[1] / abs_x_d]
     
        print((x_d))
        if r <= limit:
            reily(A, x_d)
        else:
              print("結果は{}です。".format(r))
A = np.array([[4,-1],[-1,4]])
x = np.array([1,0])
reily(A, x)
