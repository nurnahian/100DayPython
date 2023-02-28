# super keyword
class ParetClass:
    def parent_methode(self):
        print("This is the parent methode")

class ChildClass(ParetClass):
    def parent_methode(self):
        print("Nahian")
        super().parent_methode()

    def child_methode(self):
        print("This is the child")
        super().parent_methode()


child_object = ChildClass()
child_object.child_methode()
child_object.parent_methode()
