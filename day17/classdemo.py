class Car:
    def __init__(self, name):
        self.classname = name

    def printname(self):
        self.classname+=")"
        print(self.classname)

veron = Car("Atharv")
veron.printname()
