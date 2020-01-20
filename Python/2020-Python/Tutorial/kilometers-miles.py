# This program will convert kilometers to miles.

# Collect imput from the user

km = float(input('How many kilometers? '))

#conversion factor
conv_fac = 0.621371

miles = km * conv_fac

print('%0.3f Kilometers is equal to %0.3f miles' %(km, miles))
