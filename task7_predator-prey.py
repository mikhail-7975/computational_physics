import numpy as np
import matplotlib.pyplot as plt


def SystemOfEquations(X: np.ndarray, t = 0, a = 10, b = 2, c = 2, d = 10):
#def SystemOfEquations(X: np.ndarray, t=0, a=1., b=1., c=1., d=1.):
    x = np.float64(X[0])
    y = np.float64(X[1])
    return np.array([a * x - b * x * y,
                    c * x * y - d * y])

def RungeKutt_Method_2(leftBorder, rightBorder, X_t0: np.array, __step, alpha):
    res_vect_list = [np.array(X_t0)]
    time = leftBorder
    while time < rightBorder:
        res_vect_list.append(res_vect_list[-1] + __step *
                      ((1 - alpha) * SystemOfEquations(X=res_vect_list[-1], t=time) +
                       alpha * SystemOfEquations(X=( res_vect_list[-1] + __step / (2 * alpha) * SystemOfEquations(X=res_vect_list[-1], t = time) ), t = time + __step / (2 * alpha))))
        time += __step
    return res_vect_list


X = RungeKutt_Method_2(0, 2, [10, 10], 0.01, 0.75)


x = []
y = []


#plt.axis()
'''
for i in range(0, 1000):
    #plt.xlim(0, 3)
    #plt.ylim(0, 3)
    x.append(X[i][0])
    y.append(X[i][1])
    print(x)
    print(y)
    plt.plot(x, y,)
    plt.show()
'''
x, y = [x[0] for x in X], [x[1] for x in X]


plt.plot(x, 'x')
plt.plot(y, 'o')
plt.show()
plt.plot(x, y)
plt.show()
#print(Y)

