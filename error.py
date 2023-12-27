#Devuelve error -> ZeroDivisionError
#print(0/0)
'''
print('Hola 1')
suma = lambda x,y: x + y
assert suma(2,2) == 4

print('Hola 2')

age = 10
if age < 18:
    raise Exception('No se permiten menores de edad')
'''
#Uso de manejo de errores -> si pasa un error, puede proceder con el codigo
try:
    print(0/0)
except ZeroDivisionError as error:
    print('Error')

print('hola')
