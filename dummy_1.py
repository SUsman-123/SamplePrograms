# statistics

n_a = [[1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0]]
print(n_a)

array_stats = [[3, 2, 1, 8], [4, 5, -6, 0]]

print(np.min(array_stats))
print(np.min(array_stats, axis=0))
print(np.min(array_stats, axis=1))

print(np.max(array_stats))
print(np.max(array_stats, axis=1))

print(np.sum(array_stats, axis=1))
print(np.sum(array_stats, axis=0))

# reshape

array_stats = np.array([[1, 2, 3, 7], [4, 5, -6, 4]])

print(array_stats.reshape((4, 2)))

# stacking

a_v1 = np.array([1, 2, 3])

a_v2 = np.array([1, 2, 3])

a_v3 = np.array([7, 8, 9])

print(np.array([a_v1, a_v2, a_v3]))

print(np.hstack([a_v1, a_v2, a_v3]))

# arange - array range

one_d = np.arange(6)
print(one_d)

two_dim = np.arange(12).reshape(4, 3)
print(two_dim)
print(two_dim.shape)

three_dim = np.arange(24).reshape(2, 3, 4)
print(three_dim)
print(three_dim.shape)

print(np.arange(5))

array_one = np.array([10, 20, 30, 40])
array_two = np.arange(10, 50, 10)

print(array_one * array_two)  # array multiplication
print(array_one @ array_two)  # matrix multiplication -- sum of final elements
print(array_one.dot(array_two))

print(array_two)

print(array_two - array_one)

# nupmy array as a list

array_l = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 23, 45, 6, 7])

# numpy arrays can be indexed as list

print(array_l[[1, 3, 5, 7, 4]])



############################################################



data_from_text_file = np.genfromtxt('Numpy_Data.txt' ,delimiter= ',')

print(data_from_text_file)

data_from_text = data_from_text_file.astype('int32')
print(data_from_text)

print(data_from_text > 10)
# advance indexing

print(data_from_text[data_from_text > 0])


print(data_from_text[data_from_text < 0])
# fill values

fill_values = np.genfromtxt('Numpy_Data.txt' ,delimiter= ',', dtype=np.int32)
print(fill_values)

fill_values = np.genfromtxt('Sample_1.txt' ,delimiter= ',', dtype=np.int32, filling_values = 100)
print(fill_values)


import numpy as np
def numpy_function(x,y):
    return 10 * x + y
b = np.fromfunction(numpy_function, (4, 5 ), dtype=int )
print(b)