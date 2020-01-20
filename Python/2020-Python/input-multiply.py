# Python program to print the multiplication table of a number

num = int(input("Enter the number: "))

print("Multiplcation Table of ", num)
for i in range(1, 11):
    print(num, "X",i,"=",num * i)