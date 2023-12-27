#para poder usar reduce, se importa esta biblioteca
import functools

numbers = [1,2,3,4]

#lo que hace la funcion lambda es -> el contador vale 3(2+1) y la posicion es 2 y se mueve al siguiente
result = functools.reduce(lambda counter, item : counter + item, numbers)
print (result)

names = {'Nicolas', 'Miguel', 'Juan', 'Nicolas'}
print(names)