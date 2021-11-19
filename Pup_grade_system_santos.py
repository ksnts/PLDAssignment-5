#program loop
y = 1
while y==1:
    #program will ask the user to input a grade
    intGrade = input("Input Grade Percentage: ")
    #inputted number will be stored in 'grade' variable
    grade = (float(intGrade))

    #x will be used as the point grade value
    x = 0
#point grade function
    def point1(x):
        if grade>=97 and grade<=100:
            x = 1.00
            print("Grade/Mark: ",x)
        elif grade>=94 and grade<=96:
            x = 1.25
            print("Grade/Mark: ",x)
        elif grade>=91 and grade<=93:
            x = 1.5
            print("Grade/Mark: ",x)
        elif grade>=88 and grade<=90:
            x = 1.75
            print("Grade/Mark: ",x)
        elif grade>=85 and grade<=87:
            x = 2.00
            print("Grade/Mark: ",x)
        elif grade>=82 and grade<=84:
            x = 2.25
            print("Grade/Mark: ",x)
        elif grade>=79 and grade<=81:
            x = 2.5
            print("Grade/Mark: ",x)
        elif grade>=76 and grade<=78:
            x = 2.75
            print("Grade/Mark: ",x)
        elif grade>=65 and grade<=74:
            x = 5.00
            print("Grade/Mark: ",x)
        elif grade==75:
            x = 3.00
            print("Grade/Mark: ",x)
        else:
            print("Invalid input")
#running the function
    point1(x)

#Grade description
    if grade>=94 and grade<=100:
        print("Description: Excellent")
    elif grade>=88 and grade<=93:
        print("Description: Very Good")
    elif grade>=82 and grade<=87:
        print("Description: Good")
    elif grade>=76 and grade<=81:
        print("Description: Satisfactory")
    elif grade>=65 and grade<=74:
        print("Description: Failure")
    elif grade==75:
        print("Description: Passing")
    print ("\n")










