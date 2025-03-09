medical_cause=input("Did you have any medical cause Yes or No : ")
atten=int(input("Enter your attendence : "))
if medical_cause=='yes':
    print("You are allowed")
else:
    if atten>=75:
        print("Allowed")
    else:
        print("Not allowed")