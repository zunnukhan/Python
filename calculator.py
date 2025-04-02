def add (p,q):
    return p+q
def substract (p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide (p,q):
    return p/q
print("Please select opretion.")
print("h.add")
print("a.substract")
print("c.multiply")
print("k.divide")
choice=input("Please enter your choice (h/a/c/k:)")
num1=int(input("Please enter your first number :"))
num2=int(input("Please enter your second number :"))
if choice=="h":
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=="a":
    print(num1,"-",num2,"=",substract(num1,num2))
elif choice=="c":
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=="k":
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("this is an invalid input")