string=input("Please enter you own word: ")
char=input("Please enter your character: ")
i=0
count=0
while(i<len(string)):
    if(string[i]==char):
        count=count+1
    i=i+1
print("The total number of times ",char,"has occured ",count)