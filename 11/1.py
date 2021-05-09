# функция, которая генерирует необходимое нам количество единиц.
def simple_generator(val):
    while val > 0:
    val -= 1
    yield 1

gen_iter = simple_generator(5)
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))

# при вызове yield функция не прекращает свою работу,
# а “замораживается” до очередной итерации, запускаемой функцией next().