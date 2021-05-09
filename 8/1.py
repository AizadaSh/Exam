from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("Passed value: ", x)
    @abstractmethod
    def task(self):
        print("We are inside Absclass task")

class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")

class example_class(Absclass):
    def task(self):
        print("We are inside example_class task")

#object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)

#object of example_class created
example_obj = example_class()
example_obj.task()
example_obj.print(200)

print("test_obj is instance of Absclass? ", isinstance(test_obj, Absclass))
print("example_obj is instance of Absclass? ", isinstance(example_obj, Absclass))
# Absclass абстрактный класс, который наследует от ABC класс из модуля ABC. Содержит абстрактный метод Задача () и а Печать () Метод, который виден пользователем. Две другие классы, наследующие из этого абстрактного класса, являются test_class и example_class Отказ У них обоих есть свои Задача () Метод (расширение абстрактного метода).
# После того, как пользователь создает объекты из обоих test_class и example_class классы и вызывают Задача () Метод для них обоих, скрытые определения для Задача () Методы внутри обоих классов вступают в игру. Эти определения являются скрытый от пользователя. Абстрактный метод Задача () из абстрактного класса Absclass на самом деле никогда не вызывает.
# Но когда Печать () Метод называется как для test_obj и example_obj , абсцкласс Печать () Способ вызывается, поскольку это не абстрактный метод.