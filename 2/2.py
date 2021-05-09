class Computer:
    
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# изменяем цену
c.__maxprice = 1000
c.sell()

# используем функцию сеттера
c.setMaxPrice(1000)
c.sell()