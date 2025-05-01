testdict={"Codingal":2,"is":3,"best":2,"for":2,"Coding":1}

print("The original Dictionary: "+str(testdict))

K=2
res=0
for key in testdict:
    if testdict[key]== K:
        res=res+1

print("Frequency of K is : "+ str(res))