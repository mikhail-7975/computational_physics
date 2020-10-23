import numpy as np
import matplotlib.pyplot as plt

def foo(x, t):
    return -x + 0 * t#1 / x#-x





#plt.plot(X, [foo(i) for i in np.arange(T1, T2 + Step / 2, Step)])
#plt.show()

def Euler_Method(leftBorder, rightBorder, x_t0, __step):
    result = [x_t0]
    time = leftBorder
    while time < rightBorder:
        result.append(result[-1] + __step * foo(x=result[-1], t=time))
        time += __step
    return result

def derivation(arr, step):
    return [(arr[i + 1] - arr[i]) / step for i in range(len(arr) - 1)]

def RungeKutt_Method_2(leftBorder, rightBorder, x_t0, __step, alpha):
    result = [x_t0]
    time = leftBorder
    while time < rightBorder:
        result.append(result[-1] + __step *
                      ((1 - alpha) * foo(x=result[-1], t=time) +
                       alpha * foo(x=(result[-1] + __step / (2 * alpha) * foo(x=result[-1], t = time)), t = time + __step / (2 * alpha))))
        time += __step
    return result

def RungeKutt_Method_4(leftBorder, rightBorder, x_t0, __step):
    result = [x_t0]
    time = leftBorder
    while time < rightBorder:
        k1 = foo(t = time, x = result[-1])
        k2 = foo(t = time + __step / 2, x = result[-1] + __step / 2 * k1)
        k3 = foo(t = time + __step / 2, x = result[-1] + __step / 2 * k2)
        k4 = foo(t = time + __step, x = result[-1] + __step * k3)
        result.append(result[-1] + __step  / 6 * (k1 + 2 * k2 + 2 * k3 + k4))
        time += __step
    return result

Step = 0.25

T1 = 0
T2 = 3

X_t0 = 1

X = np.arange(T1, T2 + Step, Step)
Y_x = Euler_Method(T1, T2, X_t0, Step)
Y_x_rk_2 = RungeKutt_Method_2(T1, T2, X_t0, Step ,0.75)
Y_x_rk_4 = RungeKutt_Method_4(T1, T2, X_t0, Step)
y_analyt = [np.exp(-i) for i in X]

err_1 = []
err_2 = []
err_3 = []
for i in range(len(X)):
    print(Y_x[i] - y_analyt[i], '\t', Y_x_rk_2[i] - y_analyt[i], '\t', Y_x_rk_4[i] - y_analyt[i])
    err_1.append(-Y_x[i] + y_analyt[i])
    err_2.append(- Y_x_rk_2[i] + y_analyt[i])
    err_3.append(- Y_x_rk_4[i] + y_analyt[i])


plt.plot(Y_x, 'x')
plt.plot(Y_x_rk_2, 'o')
plt.plot(Y_x_rk_4, 'red')
plt.plot(y_analyt, 'blue')
print()
#plt.plot(X, y_anal)
plt.show()
plt.plot(err_1, 'x')
plt.plot(err_2, 'o')
plt.plot(err_3, 'red')
plt.plot(np.zeros(len(err_3)), 'blue')
#plt.plot(y_analyt, 'blue')
print()
#plt.plot(X, y_anal)
plt.show()