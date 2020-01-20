# Three sides of the triangle are a, b, c.

a = float(input('Enter the first side: '))
b = float(input('Enter the second side: '))
c = float(input('Enter the third side: ')) 

# Calculate the semi perimeter
s = (a + b + c)/2

# Calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the traingle is %0.2f' %area)
