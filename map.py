numbers = [1,2,3,4]
numbers_v2 = []
for i in numbers:
    numbers_v2.append(i*2)

print(numbers)
print(numbers_v2)

#Utilizando map -> se puede generar la operacion de dos listas pero en menor cantidad de lineas ed codigo
numbers_v3 = list(map(lambda i : i*2, numbers))
print(numbers_v3)

#Que pasa si la dimension entre arreglos no es la misma?
numbers_1 = [1,2,3,4]
numbers_2 = [5,6,7]

result_f = list(map(lambda x, y: x+y, numbers_1, numbers_2))
print(numbers_1)
print(numbers_2)
print(result_f)