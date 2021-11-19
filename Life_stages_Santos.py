#user is prompted to input age
intAge = float(input("Input your age: "))
#if-else code to identify life stage
print("\n")
if intAge <= 12:
    print("You are a: Kid")
elif intAge <=17 and intAge>12:
    print("You are a: Teen")
elif intAge>18:
    print("You are an: Adult")
elif intAge==18:
    print("Debut Age!")