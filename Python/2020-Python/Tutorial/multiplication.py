# This will show the multiplication table of the number

num = int(input("Show the multiplication table of: "))
#using the loop to iterate multiplcation 10 times

for i in range(1,11):
    print(num,'x',i,"=",num*i)