import numpy as np
from numpy.core.numeric import ones

X = np.array([[2,3,4],[4,3,3],[4,5,3],[4,2,7]])
y = np.array([[1.4,2,2,5]]).T
one = np.ones((X.shape[0],1))

X_ngang = np.concatenate((one, X), axis = 1) #ghép ma trận

def grad(w):
    N = X_ngang.shape[0]
    return X_ngang.T.dot(X_ngang.dot(w) - y) / N

def lost(w):
     N = X_ngang.shape[0]
     return (np.linalg.norm(y-X_ngang.dot(w),2)**2)/(2*N)

def myGD(w_init, grad, nheta, epsilon, nloop = 1000):
    w = [w_init]
    for i in range(nloop):
        w_new = w[-1] - nheta * grad(w)
        if (np.linalg.norm(grad(w_new))) < epsilon:
            break
        w.append(w_new)
    return w[-1]

if __name__ == "__main__":
    w_init1 = np.array([[2],[5],[6],[1]])
    w_op = myGD(w_init=w_init1 ,nheta=0.01, epsilon= 0.01, nloop = 100)
    print(w_op)


