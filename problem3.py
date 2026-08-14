### Write a program that reads a binary number as a string (eg.  "101101") and calculates its decimal equivalent without using a built-in conversion function.
denary = 0

binary = input("Enter binary number: ")

binary_list = list(binary)

binary_list.reverse()
print(binary_list)

for i in binary_list:
    if i == '1':
        index = binary_list.index(i) #ur wrong
        print(index)
        denary += pow(2, index)


print(denary)