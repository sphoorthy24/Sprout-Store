
import numpy as np


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
	print('START Q2_D\n')
	'''
	Start writing your code here
	'''
	x = np.loadtxt("datasets/Q1_B_train.txt", dtype=str ,usecols=1).astype("float")[:20]
	y = np.loadtxt("datasets/Q1_B_train.txt", dtype=str ,usecols=-2).astype("float")[:20]
	z = np.loadtxt("datasets/Q1_C_test.txt", dtype=str ,usecols=1).astype("float")
	a = np.loadtxt("datasets/Q1_C_test.txt", dtype=str ,usecols=-2).astype("float")

	domain = z
	y_bar = [ local_weighted_regression(x0, x, y, tau=1) for x0 in domain ]

	summation = 0  
	n = len(a)
	for i in range (0,n): 
		difference = a[i] - y_bar[i] 
		squared_difference = difference**2 
		summation = summation + squared_difference 
		MSE = summation/n 
	print(MSE)


	print('END Q2_D\n')


if __name__ == "__main__":
    main()
    