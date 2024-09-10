class Transport:
    def __init__(self, brand, model, year, speed):
        self.brand = brand 
        self.model = model
        self.year = year 
        self.speed = speed 

    def start(self):
        self.speed += 10

    def stop(self):
        self.speed = 0

    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Speed: {self.speed}"


matis = Transport('Matis','honda', 1999, 600)
print(matis.get_info())
matis.start()
print(matis.get_info())
matis.stop()
print(matis.get_info())

class Car(Transport):
    def __init__(self, brand, model, year, speed,engine_type ):
        super().__init__(brand, model, year, speed)
        self.engine_type = engine_type
    def start(self):
        super().start()

    def stop(self):
        super().stop()

    def get_info(self):
        inf = super().get_info()
        return f"{inf},engine_type:{self.engine_type}"
        
car = Car('bugati','honda', 2023, 10,'Combustion engine')
print(car.get_info())
car.start()
print(car.get_info())
car.stop()
print(car.get_info())
class Bicycle (Transport):
    def __init__(self, brand, model, year, speed,type ):
        super().__init__(brand, model, year, speed)
        self.type =type
    def start(self):
        super().start()

    def stop(self):
        super().stop()

    def get_info(self):
        inf = super().get_info()
        return f"{inf},type:{self.type}"
        
bic = Bicycle('adidas','model2', 2023, 220,'mountain')
print(bic.get_info())
bic.start()
print(bic.get_info())
bic.stop()
print(bic.get_info())


class Train  (Transport):
    def __init__(self, brand, model, year, speed,carriages  ):
        super().__init__(brand, model, year, speed)
        self.carriages  =carriages 
    def start(self):
        super().start()

    def stop(self):
        super().stop()

    def get_info(self):
        inf = super().get_info()
        return f"{inf},type:{self.carriages }"
        
train = Train('train','model2', 1980, 420,60)
print(train.get_info())
train.start()
print(train.get_info())
train.stop()
print(train.get_info())