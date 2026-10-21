import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([2.1, 3.9, 4.2, 6.1, 6.8, 8.3])

w, b, lr = 0.0, 0.0, 0.02

for epoch in range(1000):
    y_hat = w * x + b                   #1 Predict
    error = y_hat - y                   #2 Calculate error
    dw = 2 * (error * x).mean()         #3 Calculate gradient
    db = 2 * error.mean()               #4 Calculate gradient

    w -= lr * dw
    b -= lr * db

plt.scatter(x, y)
plt.plot(x, w * x + b)
plt.show()
    