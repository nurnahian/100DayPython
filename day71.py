# x = [1, 2, 3, 4]
x = (1, 2, 3, 4)
print(dir(x))
print(x.__add__)

class Persone:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.version = 1


p = Persone("John",30)
print(p.__dict__)

print(help(Persone))
