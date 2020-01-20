# Declare a variable and initialize it.

f = 101;
print(f)

# Global vs local variables in functions

def someFunction():
    global f
    print(f)
    f = "Changing global variable"

someFunction()
print(f)