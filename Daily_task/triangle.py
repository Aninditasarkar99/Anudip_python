# Python program to find the area of a triangle whose sides are given
# 01/11/2023
a = 5
b = 6
c = 7

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area_of_triangle = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f'%area_of_triangle)

# output -- The area of the triangle is 14.70