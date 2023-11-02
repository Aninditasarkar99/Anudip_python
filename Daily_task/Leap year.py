''' Python program to check leap year.
'''

year = int(input("Enter a year: "))

if (year % 400 == 0) and (year % 100 == 0):
    print("Is a leap year", year)


elif (year % 4 == 0) and (year % 100 != 0):
    print("Is a leap year", year)

else:
    print("Is not a leap year", year)

''' OUTPUT - 
Enter a year: 2020
Is a leap year 2020
'''