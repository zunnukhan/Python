string=str(input("Enter the string you want to reverse : "))
string2=("")
for i in string:
    string2=i+string2
print("\n The original string",string)
print("\nThe reversed string",string2)
for i in range(10,1,-1):
    print(i)