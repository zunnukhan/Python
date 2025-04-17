import random 
playing=True
number=str(random.randint(39,44))
print("Iwill generate a number between 39 to 44,and you have to guess the number one digit at a time.")
while playing:
    guess=input("Give me your best guess \n")
    if number == guess:
        print("You win the game")
        print("The number was ",number)
        break
    else:
        print("your guess was not right,try again.\n")