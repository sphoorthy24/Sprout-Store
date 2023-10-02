import numpy as np
import matplotlib.pyplot as plt 

def local_weighted_regression(x0, X, Y, tau):
    # add bias term
    x0 = np.r_[1, x0]
    X = np.c_[np.ones(len(X)), X]
     
    # fit model: normal equations with kernel
    xw = X.T * weights_calculate(x0, X, tau)
    theta = np.linalg.pinv(xw @ X) @ xw @ Y
    # "@" is used to
    # predict value
    return x0 @ theta
 
# function to perform weight calculation
def weights_calculate(x0, X, tau):
    return np.exp(np.sum((X - x0) ** 2, axis=1) / (-2 * (tau **2) ))

def main():
    print('START Q2_AB\n')

    x = np.loadtxt("datasets/Q1_B_train.txt", dtype=str ,usecols=1).astype("float")
    y = np.loadtxt("datasets/Q1_B_train.txt", dtype=str ,usecols=-2).astype("float")
    z = np.loadtxt("datasets/Q1_C_test.txt", dtype=str ,usecols=1).astype("float")
    
    domain = z
    predicted = [ local_weighted_regression(x0, x, y, tau=1) for x0 in domain ]
        
    plt.figure(figsize = (8, 5))
    m, b = np.polyfit(x, y, 1)
    plt.plot(z, m*z+b, color = '#f25f5c')
    plt.scatter(x, y, color = 'red')
    plt.title('Predicted values by Linear Regression', fontsize = 15)
    plt.xlabel('Resulting function with the data points')
    plt.ylabel('price')
    plt.scatter(z, predicted, color = "#247ba0")
    plt.show()

    print('END Q2_AB\n')


if __name__ == "__main__":
    main()
