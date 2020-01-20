# Program to convert fahrenheit to celsius

fah = float(input('Enter the temperature in Fahrenheit: '))

# Calculate the temperature in Celicus

cel = (fah - 32) / 1.8

print('%f Fahrenheit is equal to %0.1f degree Celcius' %(fah, cel))