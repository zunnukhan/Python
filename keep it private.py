class myclass:
     __privateVar=27
     def __privateMeth(self):
          print("I'am inside class myclass")

     def hello(self):
        print("Private Variable value: ",myclass.__privateVar)

foo=myclass()
foo.hello()
foo.__privateMeth