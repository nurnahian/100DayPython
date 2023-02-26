class Persone:
    # constractor
    def __init__(self, name,occ,age):
        self.name = name
        self.occ = occ
        self.age = age

    def info(self):
        print(f"{self.name} is a {self.occ} {self.age}")


a = Persone("Nur","student",24)

a.info()
