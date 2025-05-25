class Person(object):

    def __init__(self,name,idnum):
        self.name=name 
        self.idnum=idnum
    def display(self):
            print(self.name)
            print(self.idnum)

#child class
class Employee(Person):
    def __init__(self,name,idnum,salary,post):
        self.salary=salary
        self.post=post
    #invoking the__init__fo the  parent
        Person.__init__(self,name,idnum)
a=Employee("Rahul" ,886012,200000,"Intern")
a.display()