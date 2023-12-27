'''
#Se declara un array vacio y en el ciclo for se le agregan elementos uno detras de otro
numbers = []
for element in range(1,11):
    numbers.append(element)
print(numbers)

#forma corta de crear una lista -> iterador for iterador incrementar en un rango de 
numbers_v2 = [element for element in range(1,11)]
print(numbers_v2)
'''
#Se declara un array vacio y en el ciclo for solo se muestran los numeros pares del rango mostrado
numbers = []
for element in range(1,11):
    if element % 2 == 0:
        numbers.append(element)

print(numbers)
#Forma 'rapida' de crear una lista -> iterador y con un condicional
numbers_v2 = [element for element in range(1,11) if ( element % 2 == 0)]
print(numbers_v2)

