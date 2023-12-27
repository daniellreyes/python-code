#slicing -> sacar ciertas partes del texto; consta de un inicio y un fin
text="Yo se Python"
#toma del elemento 0 al 5
print(text[0:5])
#Sino tiene un inicio, se toma desde el cero | si es el ultimo, coso contrario
print(text[:3])
print(text[3:])
#Consulta desde una posicion dada hasta el final, dando saltos
print(text[::3]) #aqui, mostraria todo el codigo, con saltos de 3 -> YsPh

print(4!=10)
'''

population = 0
while population < 8.85:
    population  = population + 0.05
    print("La poblacion es menor a la esperada")

print("La poblacion es de 8.85 millones de habitantesß")

'''

name = 'Mario Salvador'
name = name.replace('Mario', 'Juan')
print(name)

print(True and False)
print(8000 > 3330)
