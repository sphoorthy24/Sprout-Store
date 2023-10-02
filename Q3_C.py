import numpy as np 

class LogisticRegression:
	def __init__(self, lr=0.01, num_iter=100000, fit_intercept=True, verbose=False):
		self.lr = lr
		self.num_iter = num_iter
		self.fit_intercept = fit_intercept
	
	def __add_intercept(self, X):
		intercept = np.ones((X.shape[0], 1))
		return np.concatenate((intercept, X), axis=1)
    
	def __sigmoid(self, z):
		return 1 / (1 + np.exp(-z))

	def __loss(self, h, y):
		return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()
	
	def fit(self, X, y):
		if self.fit_intercept:
			X = self.__add_intercept(X)
        
        # weights initialization
		self.theta = np.zeros(X.shape[1])
		for i in range(self.num_iter):
			z = np.dot(X, self.theta)
			h = self.__sigmoid(z)
			gradient = np.dot(X.T, (h - y)) / y.size
			self.theta -= self.lr * gradient
			
			if( i % 10000 == 0):
				z = np.dot(X, self.theta)
				h = self.__sigmoid(z)
				print(f'loss: {self.__loss(h, y)} \t')
	
	def predict_prob(self, X):
		if self.fit_intercept:
			X = self.__add_intercept(X)	
		return self.__sigmoid(np.dot(X, self.theta))
	
	def predict(self, X, threshold):
		return self.predict_prob(X) >= threshold


def main():
	print('START Q3_C\n')
	'''
	Start writing your code here
	'''
	h = np.loadtxt("datasets/Q3_data.txt", dtype=str ,usecols=1)
	h = np.array([x[:-2] for x in h]).astype(float)
	w = np.loadtxt("datasets/Q3_data.txt", dtype=str ,usecols=2)
	w = np.array([x[:-2] for x in w]).astype(float)
	a = np.loadtxt("datasets/Q3_data.txt", dtype=str ,usecols=3)
	a = np.array([x[:-2] for x in a]).astype(float)
	t = np.loadtxt("datasets/Q3_data.txt", dtype=str ,usecols=4)
	
	feature = np.stack((h,w,a),axis=1)
	target=[]
	for i in t:
		if i=='W':
			target.append(1)
		else:
			target.append(0)

	model = LogisticRegression(lr=0.01, num_iter=3000)
	model.fit(feature, np.array(target))

	preds = model.predict(feature,0.5)
	summation = 0  
	n = len(preds)
	for i in range (0,n): 
		difference = target[i] - preds[i] 
		squared_difference = difference**2 
		summation = summation + squared_difference 
		MSE = summation/n 
	print(MSE)
	
	print('END Q3_C\n')


if __name__ == "__main__":
    main()
    