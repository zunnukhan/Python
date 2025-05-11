import random
x=100
attempts=0
max_attempts=6
print("you have 6 attempts")
print ("The number is chosen between 0 to 100.")

number =random.randint(0,x)
if number %2==0:
    print("hint: THe number is even.")
else:
    print("Hint: The umber is odd.")
print("Go ahead!")
while attempts<max_attempts:
    try:
        user_input=int(input("Enter your Guess:"))
        attempts+=1
        if user_input==number:
            print("Your guess is correct✅")
            print("Your guessed it in",attempts,"attempt(s)")
            break
        elif user_input>number:
            print("Your guess is too high. Try a lower number👇")
        
        else:
            print("Your guess is too low.Try a higher number☝️")
        print("You have",max_attempts-attempts,"Attempts left.")

    except:
        print("Invalid input.Pleaseenter a number.")

if user_input !=number:
    print("You could not guess the number in 6 attempts. Try again😭")
    print("The correct number was",number)