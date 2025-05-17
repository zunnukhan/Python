class Dog:
    species="dog"

    def __init__(self,name,age): 
        self.name=name
        self.age=age

LadradorRetriever=Dog("Ladrador Retriever",5)
GermanShepherd=Dog("German Shepherd",7)
GoldenRetriever=Dog("Golden Retriever",8)

print("Ladrador Retriever is a ",LadradorRetriever.species)
print(LadradorRetriever.name,"is",LadradorRetriever.age,"years old")
print()
print("German Shepherd is also a ",GermanShepherd.species)
print(GermanShepherd.name,"is",GermanShepherd.age,"years old")
print()
print(" Golden Retriever is also a ",GoldenRetriever.species)
print(GoldenRetriever.name,"is",GoldenRetriever.age,"years old")
