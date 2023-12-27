import random

countries = {'col', 'mex', 'bol'}
populationv2 = { country: random.randint(1,100) for country in countries}
print(populationv2)
#Utilizando dictionary comprehension con if
# Hay que verlo en tres etapas. En el primero declarar llave/valor, el segundo el ciclo | el tercero la condicion
result = { country: population for (country, population) in populationv2.items() if population > 40 }
print(result)

text='Hola soy Daniel'
unique = { c: c.upper() for c in text if c in 'aeiou' }
print(unique)