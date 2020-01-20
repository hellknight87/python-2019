# Program to find LCM of a number

def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

print("The LCM of ",num1,"and",num2,"is",lcm(num1, num2))