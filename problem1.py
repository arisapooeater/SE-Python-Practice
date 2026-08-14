### Write a program that reads three three test scores as input, calculates the average, and prints "Pass" if the average is 50 or above, otherwise "Fail". Print the average as well

score1 = int(input("Test Score 1: "))
score2 = int(input("Test Score 2: "))
score3 = int(input("Test Score 3: "))

average = (score1 + score2 + score3)/3

if average >= 50:
    print("Pass")
else:
    print("Fail")

print(average)