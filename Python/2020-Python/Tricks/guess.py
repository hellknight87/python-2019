import random
n = random.randint(1,99)

guess = int(input("Enter an integer from 1 to 99.: "))
while n != "guess":
    print
    if guess < n:
        print ("Guess is low")
        guess = int(input("Ener an integer from 1 to 99."))
    elif guess > n:
        print ("Guess is high.")
        guess = int(input("Ener an integer from 1 to 99."))
    else:
        print ("You guessed it right!: ")
        break
    print