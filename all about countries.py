class India():
    def capital(self):
        print("New delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language in India.")

    def  type(self):
        print("India is a devoloping country.")

#class 2
class USA():
    def capital(self):
        print("Washinton DC is the capital of India.")

    def language(self):
        print("English is the most widely spoken language in India.")

    def  type(self):
        print("USA is a devoloped country.")

obj_ind=India()
obj_usa=USA()

for country in (obj_ind,obj_usa):
    country.capital()
    country.language()
    country.type()