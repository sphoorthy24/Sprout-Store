
import numpy as np

def linear(X, b0, b1):
    return [b0+b1*x for x in X]

# b0 - Intercept
def intercept(X, Y, b1): 
    x_ = np.mean(X)
    y_ = np.mean(Y)
    
    return y_-b1*x_

# b1 - Slope
def slope(X, Y):
    x_ = np.mean(X)
    y_ = np.mean(Y)
    
    rise = sum([(x-x_) * (y-y_) for x,y in zip(X,Y)])
    run = sum([(x-x_)**2 for x,y in zip(X,Y)])
    
    return rise / run

def main():
	print('START Q1_D\n')
	'''
	Start writing your code here
	'''
	x = np.loadtxt("datasets/Q1_B_train.txt", dtype=str ,usecols=1).astype("float")[:20]
	y = np.loadtxt("datasets/Q1_B_train.txt", dtype=str ,usecols=-2).astype("float")[:20]
	
	z = np.loadtxt("datasets/Q1_C_test.txt", dtype=str ,usecols=1).astype("float")
	a = np.loadtxt("datasets/Q1_C_test.txt", dtype=str ,usecols=-2).astype("float")

	b1 = slope(x, y)
	b0 = intercept(x, y, b1)
	y_bar = linear(z, b0, b1)

	summation = 0  
	n = len(a)
	for i in range (0,n): 
		difference = a[i] - y_bar[i] 
		squared_difference = difference**2 
		summation = summation + squared_difference 
		MSE = summation/n 
	print(MSE)

	print('END Q1_D\n')


if __name__ == "__main__":
    main()