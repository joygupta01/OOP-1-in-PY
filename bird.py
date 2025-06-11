class Parrot :
    species = "birds"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sing(self,song):
        print(f"{self.name} sings {song}")  

obj1 = Parrot("Woo",2)

obj2 = Parrot("Huu",5)


print(f"The Woo is{obj1.species}")

print(f"{obj1.name} is {obj1.age} years old")
print(f"{obj2.name} is {obj2.age} years old")
obj1.sing("Happy")