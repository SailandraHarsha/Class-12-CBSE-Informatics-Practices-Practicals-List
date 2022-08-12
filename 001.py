import numpy as np

#Create Array
arr = np.array(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
print('Print all values:')
#Print Array
print(arr)
print('\nPrint all values using loop:')
#print Array in loop
for i in range(0, len(arr)):
    print(arr[i])

print('\nAll elements, slice elements from index 1 to index 2 (not included):')
#Print sliced Array in loop
for i in range(0, len(arr)):
    print(arr[i, 1:2])
