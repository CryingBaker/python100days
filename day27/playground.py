def add(*numbers):
    sum = 0
    for number in numbers:
        sum+=number
    return sum

print(add(1,58,6,8,12,54))

def calculate(**kwargs):
    for (key,value) in kwargs.items():
        print(key,value)

calculate(add=1,multiply=5)  


class Car:
    def __init__(self,**kw):
        self.model = kw.get("model")
        self.price = kw["price"]

car = Car(price="45000")

print(car.model)
print(car.price)