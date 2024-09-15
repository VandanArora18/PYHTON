import numpy as np
#qus 1.1
np1= np.arange(5,26)
print(np1)

#qus1.2
np2 = np.random.randint(10, 51, (3, 4))
print("2D array:\n", np2)


#qus2.1 
print("Shape:", np1.shape)
print("Size:", np1.size)
print("Data type:", np1.dtype)



#qus2.2
print("Shape:", np2.shape)
print("Size:", np2.size)
print("Data type:", np2.dtype)


#qus 3.1
array1 = np.array([2, 4, 6, 8, 10])
array2 = np.array([1, 3, 5, 7, 9])

#qus3.2
print("Addition:", array1 + array2)
print("Subtraction:", array1 - array2)
print("Element-wise multiplication:", array1 * array2)
print("Element-wise division:", array1 / array2)




#qus 4.1
np3 = np.arrange(1,10).reshape(3,3)
print(np3)
#qus 4.2
np4 = np3*5
print(np4)


#qus5.1
np5 = np.arange(10, 26).reshape(4, 4)
#qus 5.2 
second_row = np5[1, :]
last_column = np5[:, -1]
print("Second row:", second_row)
print("Last column:", last_column)

#qus5.3 
np5[0, :] = 0
print("Modified array:\n", np5)



#qus6.1
np6 = np.random.randint(20, 41, 10)

#qus 6.2 
elements_greater_than_30 = np6[np6 > 30]
print("Elements greater than 30:", elements_greater_than_30)




#qus7.1
np7 = np.arange(11, 23)

#qus 7.2 
array2d = np7.reshape(3, 4)
print("Reshaped array:\n", array2d)



#qus8.1
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

#qus 8.2 
print("Matrix multiplication:\n", np.dot(matrix_a, matrix_b))
print("Transpose of Matrix A:\n", matrix_a.T)




#qus 9.1
np8 = np.random.randint(10, 61, 15)

#qus 9.2 
mean = np.mean(np8)
median = np.median(np8)
std_dev = np.std(np8)
print("Mean:", mean)
print("Median:", median)
print("Standard deviation:", std_dev)

#qus10.1
matrix_a = np.array([[2, 1, 3], [0, 5, 6], [7, 8, 9]])

#qus10.2 
determinant = np.linalg.det(matrix_a)
inverse = np.linalg.inv(matrix_a)
eigenvalues, eigenvectors = np.linalg.eig(matrix_a)


