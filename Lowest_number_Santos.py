#user is prompted to enter the given numbers
int1 = input("Input first number: ")
int2 = input("Input second number: ")
int3 = input("Input third number: ")

print("\n")
#If-else statement to find the lowest num
if int1 < int2 and int1 < int3:
    print("Lowest number is: ", int1)
elif int2 < int1 and int2 < int3:
    print("Lowest number is: ", int2)
elif int3 < int1 and int3 < int2:
    print("Lowest number is: ", int3)



