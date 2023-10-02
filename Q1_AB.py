
import numpy as np
import matplotlib.pyplot as plt

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
	print('START Q1_AB\n')
	'''
	Start writing your code here
	'''
	x = np.loadtxt("datasets/Q1_B_train.txt", dtype=str ,usecols=1).astype("float")
	y = np.loadtxt("datasets/Q1_B_train.txt", dtype=str ,usecols=-2).astype("float")
	z = np.loadtxt("datasets/Q1_C_test.txt", dtype=str ,usecols=1).astype("float")

	b1 = slope(x, y)
	b0 = intercept(x, y, b1)
	predicted = linear(z, b0, b1)

	file = open("datasets/prediction.txt", "w+")
	content = ' {} {}'.format(b0,b1)
	file.write(content)
	file.close()

	plt.figure(figsize = (8, 5))
	plt.plot(x, b1*x+b0, color = '#f25f5c')
	plt.scatter(x, y, color = '#f25f5c')
	plt.title('Predicted values by Linear Regression', fontsize = 15)
	plt.xlabel('Resulting function with the data points')
	plt.ylabel('price')
	plt.scatter(z, predicted, color = "#247ba0")
	plt.show()

	print('END Q1_AB\n')


if __name__ == "__main__":
    main()