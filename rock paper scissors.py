import random
option=["rock","paper","scissor"]
while True:
    useraction=input("Enter a choicerock,paperor scissor : ")
    computerchoice=random.choice(option)
    print("You chose:",useraction)
    print("computer chose:",computerchoice)
    if useraction==computerchoice:
        print("It's tie")
    elif useraction=="Rock"and computerchoice=="scissors":
        print("Rock smashes scissors ! you win")
    elif useraction=="paper"and computerchoice=="Rock":
        print("paper covers rock .You win")
    elif useraction=="scissor"and computerchoice=="paper":
        print("Scissor cuts paper . You win")
    else:
        print("You lose!")