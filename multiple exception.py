try:
    num1,num2=eval(input("enter two numbers,separeted by a comma : "))
    result=num1/num2
    print("result is",result)
except ZeroDivisionError:
    print("division by zero ir error!")
except SyntaxError:
    print("Comma is missing.Enter numbers separeted by comma like this  1,2")
except:
    print("wrong input")
else:
    print("No exceptions")
finally:
    print("this will execute no matter what")