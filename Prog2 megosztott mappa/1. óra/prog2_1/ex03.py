# 3. Exercise
# Write a Python program which takes two digits m (row) and n (column)
# as input and generates a two-dimensional array. The element value in
# the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1.
# Test Data : Rows = 3, Columns = 4
# Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

import numpy as np

n = int(input("n (rows): "))
m = int(input("m (cloumns): "))
mtx = np.zeros((n,m),np.int32)

print("\n(np.zeros(n,m) eredménye:)")
print(mtx)

print("\n(feltöltés után)")
for i in range(n):
    for j in range(m):
        mtx[i][j] = i*j

print(mtx)