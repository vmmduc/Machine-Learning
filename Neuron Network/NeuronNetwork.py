import numpy as np
import matplotlib.pyplot as plt

eta = 0.01

# input
x = np.array([[0,0],[1,0],[1,1],[0,1]], np.float32)
# label
y = np.array([0,0,1,0], np.float32)

# init weight
w = np.zeros(2, np.float32)
b = np.zeros(1,np.float32)

for k in range(1000):
    y_hat = x.dot(w) + b
    y_hat = 1.0/(1.0 + np.exp(-y_hat))
    err = y - y_hat
    # cap nhat trong so
    w_hat = np.transpose(x).dot(err)
    b_hat = np.sum(err)
    w = w + eta * w_hat
    b = b + eta * b_hat

plot_x = np.array([np.min(x[:,0] - 0.2), np.max(x[:,1] + 0.2)])
plot_y = -1 / w[1] * (w[0] * plot_x + b)
print('w = ' + str(w))
print('b = ' + str(b))
print('plot_y = ' + str(plot_y))
plt.scatter(x[:, 0], x[:, 1], c=y, s=100, cmap='viridis')
plt.plot(plot_x, plot_y, color = 'k', linewith = 2)
plt.xlim([-0.2, 1.2])
plt.ylim([-0.2,1,2])