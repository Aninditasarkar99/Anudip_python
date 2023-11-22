'''
1. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
'''
import numpy as np

list = [np.array([3,2,8,9]), np.array([4,12,34,25,78]), np.array([23,12,67])]
new_list=[]

for i in list:
    arra1st = i
    mean = np.mean(i)
    new_list.append(mean)
print("The mean of every numpy array in the given list is:" , new_list)

'''
OUTPUT -
The mean of every numpy array in the given list is: [5.5, 30.6, 34.0]
'''