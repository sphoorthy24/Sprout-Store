import numpy as np
def linear(X, b0, b1):
    return [b0+b1*x for x in X]

def main():
	print('START Q1_C\n')
	'''
	Start writing your code here
	'''

	y= np.loadtxt("datasets/Q1_C_test.txt", dtype=str ,usecols=1).astype("float")
	z = np.loadtxt("datasets/Q1_C_test.txt", dtype=str ,usecols=-2).astype("float")

	weights1 = np.loadtxt("datasets/prediction.txt", dtype=float ,usecols=0).astype("float")
	weights2 = np.loadtxt("datasets/prediction.txt", dtype=float ,usecols=1).astype("float")


	y_bar = linear(y, weights1,weights2)

	summation = 0  
	n = len(z)
	for i in range (0,n): 
		difference = z[i] - y_bar[i] 
		squared_difference = difference**2 
		summation = summation + squared_difference 
		MSE = summation/n 
	print(MSE)
	print('END Q1_C\n')


if __name__ == "__main__":
    main()
    