import numpy as np
import matplotlib.pyplot as plt

A = np.array([[998, 1998], [-999, -1999]]) #matrix of differential equation system

def Explicit_Euler_method(leftBorder, rightBorder, X_t0: np.array, __step): #accuracy O(h^1)
    res_vect_list = [np.array(X_t0)]
    time = leftBorder
    while time < rightBorder:
        res_vect_list.append(res_vect_list[-1] + __step * A.dot(res_vect_list[-1]))
        time += __step
    return res_vect_list

def Implicit_Euler_method(leftBorder, rightBorder, X_t0: np.array, __step): #accuracy O(h^2)
    res_vect_list = [np.array(X_t0)]
    time = leftBorder
    while time < rightBorder:
        res_vect_list.append(np.linalg.inv(np.array([[1, 0], [0, 1]]) - __step * A).dot(res_vect_list[-1]))
        time += __step
    return res_vect_list


analyt_X = [np.array([2, -1]) * np.exp(-t) + np.array([1, -1]) * np.exp(-1000 * t) for t in np.arange(0, 1, 0.001)]
X = Implicit_Euler_method(0, 1, X_t0=[3, -2], __step=0.1)
X1 = Explicit_Euler_method(0, 1, X_t0=[3, -2], __step=0.001)


x_imp, y_imp = [x[0] for x in X], [x[1] for x in X]
x_expl, y_expl = [x[0] for x in X1], [x[1] for x in X1]
x_an, y_an = [x[0] for x in analyt_X], [x[1] for x in analyt_X]


plt.plot(np.linspace(x_expl[0], x_expl[-1], len(x_expl)), x_expl, 'x-', label ="Explicit")
plt.plot(np.linspace(x_an[0], x_an[-1], len(x_an)), x_an, '-', label ="Analytical")
plt.plot(np.linspace(x_imp[0], x_imp[-1], len(x_imp)), x_imp, 'o-', label ="Implicit")
plt.legend()
plt.show()

plt.plot(np.linspace(y_expl[0], y_expl[-1], len(y_expl)), y_expl, 'x-', label ="Explicit")
plt.plot(np.linspace(y_an[0], y_an[-1], len(y_an)), y_an, '-', label ="Analytical")
plt.plot(np.linspace(y_imp[0], y_imp[-1], len(y_imp)), y_imp, 'o-', label ="Implicit")
plt.legend()
plt.show()

plt.plot(x_expl, y_expl, 'x-',label ="Explicit")
plt.plot(x_an, y_an, label ="Analytical")
plt.plot(x_imp, y_imp, 'o-', label ="Implicit")
plt.legend()
plt.show()