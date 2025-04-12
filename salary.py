expirence=int(input("enter your expirence : "))
def salary(expirence):
    if expirence < 2:
        print("Your salary is ₹25,000")
    elif expirence > 2:
        print("Your salary is ₹50,000")
    elif expirence > 5:
        print("Your salary is ₹70,000")
    else:
        print("Your salary is ₹1,00,000")