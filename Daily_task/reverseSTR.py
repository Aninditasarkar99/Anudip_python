'''
Write a Python program to reverse words in a string
String = “Deeptech Python Training”
'''


# input string
string = "Deeptech Python Training"
# reversing words in a given string
words = string.split(' ')
rev = ' '.join(reversed(words))
print("reverse: ", rev)


'''
OUTPUT - 
reverse:  Training Python Deeptech
'''