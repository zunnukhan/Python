number1=[1,2,3,4]
number2=[5,6,7,8]
result=map(lambda x,y: x+y,number1,number2)
print("Addition of two lists")
print(list(result))

num=[1,2,3,4,5]
def sq(n):
    return n*n
square=list(map(sq,num))
print("Square of numbers in list")
print(square)