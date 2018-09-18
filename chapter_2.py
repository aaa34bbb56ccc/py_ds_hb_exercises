import numpy as np

print(np.__version__)

L = list(range(10))

type(L[0])

L2 = [str(c) for c in L]

type(L2[0])

L3 = [True, "2", 3.0, 4]

[type(item) for item in L3]

import array

L = list(range(10))

A = array.array('i', L)

A1 = np.array([1,4,2,5,3])

A2 = np.array([3.14, 4, 2, 3])

A3 = np.array([1,2,3,4], dtype='float32')

A4 = np.array([range(i, i+3) for i in [2,4,6]])

A5 = np.zeros(10, dtype='int')

A6 = np.ones((3, 5), dtype=float)

A7 = np.full((3, 5), 3.14)
# Create an array filled with a linear sequence
# Starting at 0, ending at 20, stepping by 2
# (this is similar to the built-in range() function)
A08 = np.arange(0, 20, 2)
# Create an array of five values evenly spaced between 0 and 1
A8 = np.linspace(0, 1, 5)
# Create a 3x3 array of uniformly distributed
# random values between 0 and 1
A9 = np.random.random((3, 3))
# Create a 3x3 array of normally distributed random values
# with mean 0 and standard deviation 1
A10 = np.random.normal(0, 1, (3, 3))
# Create a 3x3 array of random integers in the interval [0, 10)
A11 = np.random.randint(0, 10, (3,3))
# Create a 3x3 identity matrix
A12 = np.eye(3)
# Create an uninitialized array of three integers
# The values will be whatever happens to already exist at that
# memory location
A13 = np.empty(3)

a1=np.zeros(10, dtype='int16')

a2=np.zeros(10, dtype=np.int16)

