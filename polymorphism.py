class oops:
    def display(self):
        print("Welcome to")


class Method(oops): 
    def display(self):
        super().display()
        print("PYTHON")


class OverRide(Method):
    def display(self):
        super().display()
        print("Class")


r = OverRide()
r.display()
