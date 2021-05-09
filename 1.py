class Parrot:
    
    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# общий интерфейс
def flying_test(bird):
    bird.fly()

#создаем объекты
blu = Parrot()
peggy = Penguin()

# передаем объекты
flying_test(blu)
flying_test(peggy)
# определили два класса: Parrot и Penguin .
# У каждого из них есть общий метод  fly(), но они разные.

# Чтобы реализовать полиморфизм, создали общий интерфейс. 
# То есть, функцию flying_test(), которая может принимать любой 
# объект. Затем мы передали объекты blu и peggy в функцию 
# flying_test().

