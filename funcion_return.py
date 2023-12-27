#utilizando el return || Verlo así: El return puede ser asignado a una variable fuera de la funcion
def sum_with_range(min, max):
    sum=0
    for x in range(min, max):
        sum += x
    return sum

result = sum_with_range(3,6)
print(result)
result = sum_with_range(1,3)
print(result)