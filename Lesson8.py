medical_cause=input("Did you have a medical cause Y or N?: ")
attendance=int(input("Enter the attendance of the student?: "))

if medical_cause == 'Y':
    print ("You are allowed too")
else:
    if attendance>=75:
        print("You are allowed too")
    else:
        print("You are not allowed to")
