import random

class fruitquiz:

    def __init__(self):
        self.fruit={"apple":"red",
                    "mango":"yello",
                    "grapes":"black",
                    "watermelon":"green"}
        
    def quiz(self):
        while(True):
            fruit,color=
random.choice(list(self.fruit.items()))
            
print("What is the color of{}".format(fruit))
user_answer=input()
if(user_answer.lower()==color):
    print("Correct answer")
else:
    print("wrong answer")

    option=int(input("Enter 0 if you wnt to play again otherwise enter 1: "))
    if (option):
        break
print("welcome to fruite quiz")
fq=fruitquiz()
fq.quiz
