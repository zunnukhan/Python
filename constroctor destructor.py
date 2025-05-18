class Employee:

    def __init__(self,name):
        self.name=name
        print("Employee created")

    def __del__(self):
            print("Destructor Called")

obj=Employee("Zunairah")
del obj
print(obj.name)