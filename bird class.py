class Parrot:
    species="bird"

    def __init__(self,name,age): 
        self.name=name
        self.age=age

blu=Parrot("Blu",10)
woo =Parrot("Woo",15)
moyna=Parrot("Moyna",5)

print("Blu is a ",blu.species)
print("Woo is also a ",woo.species)
print("Moyna is also a ",moyna.species)

print(blu.name,"is",blu.age,"years old")
print(woo.name,"is",woo.age,"years old")
print(moyna.name,"is",moyna.age,"years old")