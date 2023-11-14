'''
Write a Python program to count and display the vowels of a given text
String=”Welcome to python Training”
'''


# take user input
String = "Welcome to python Training"
count = 0
# to check for less conditions
# keep string in lowercase
String = String.lower()
for i in String:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        # if True
        count+=1
        print("v:", i, end = "   ")
# check if any vowel found
if count == 0:
    print('\n No vowels found')
else:
    print('\n Total vowels are :' + str(count))

'''
OUTPUT- v: e   v: o   v: e   v: o   v: o   v: a   v: i   v: i   
 Total vowels are :8
'''