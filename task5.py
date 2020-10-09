import numpy as np
import matplotlib.pyplot as plt

#dpproximation function
def lagranz_polynom(x, y, pointCount):
    xnew = np.linspace(np.min(x), np.max(x), pointCount)
    result = []
    for t in xnew:
        P_n = 0
        for j in range(len(y)):
            l_x = 1
            l_x_i = 1
            for i in range(len(x)):
                if i != j:
                    l_x = l_x * (t - x[i])
                    l_x_i = l_x_i * (x[j] - x[i])
            P_n += y[j] * l_x / l_x_i
        result.append(P_n)
    return result

for i in range(4, 16):
#create original points
    n = i
    x = np.array([1 + k / n for k in range(n)])
    y = np.array([np.log(x_i) for x_i in x])
    #y[2] += 10
    #y[4] += 10
    #calculate approximation polynom
    pointNumber = 100
    xnew = np.linspace(np.min(x), np.max(x), pointNumber)
    ynew = lagranz_polynom(x, y, pointNumber)
    err = ynew - np.log(xnew)

    #draw plot
    plt.gcf().canvas.set_window_title("n = " + str(n))
    #plt.plot(x, y, 'o', xnew, ynew, 'x', xnew, np.log(xnew))
    #print(xnew)
    print('err = ', err)

    plt.grid(True)
    #plt.show()

    plt.plot(xnew, err)
    plt.show()