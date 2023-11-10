'''
Write a Python program to remove duplicate characters of a given
string.
Input = “String and String Function”
Output: String and Function '''

strings ="String and String Function"
str=""
split_str = strings.split()

for i in split_str:
    if i not in str:
        str = str + " " + i

print("Before remove:" , strings)
print("after remove" , str)
