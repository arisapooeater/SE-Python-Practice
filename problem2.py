### Write a program that stores a temperature in a variable. Using selection, print "Hot" if the temperature is above 30, "Mild" if it is between 15 and 30 inclusive, and "Cold" otherwise:

temperature = int(input("Enter temperature: "))

if temperature > 30:
    print("Hot")
elif temperature >= 15:
    print("Mild")
else:
    print("Cold")