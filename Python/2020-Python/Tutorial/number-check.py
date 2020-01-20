# Program to check if a number is postive, negative or zero

num = float(input("Enter a number: "))

if num > 0:
    print("{0} is a positive number".format(num))
elif num == 0:
    print("{0} is zero".format(num))
else:
    print("{0} is a negative number".format(num))