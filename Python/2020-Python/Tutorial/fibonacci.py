# This program prints the fibonacci sequence of the numbers.
nterms = int(input("How many terms you want?"))
# First two terms
n1 = 0
n2 = 1
count = 2
#Check if the number of terms is valid
if nterms <= 0:
    print("Please enter a postive integer")
elif nterms == 1:
    print("Fibonacci sequence:")
    print(n1)
else:
    print("Fibonacci sequence:")
    print(n1,",",n2,end=',')
    while count < nterms:
        nth = n1 + n2
        print(nth,end=',')
        # update values
        n1 = n2
        n2 = nth
        count += 1