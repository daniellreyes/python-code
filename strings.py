text = 'Yo se programar en Python'
print('Javascript' in text)
print('Python' in text)
#El operador 'in' Devuelve un true or False si la cadena JavaScript se encuentra dentro de la cadena Text
'''

if 'JavaScript' in text:
    print('Eres un crack')
else:
    print('Elejiste dos dos')

#Metodo para contar caracteres de un str --> len

size = len(text)
print(size)

'''
# con upper() convierte todo el string a MATUSCULAS, mientras que con lower(), en minusculas
print(text.upper())
print(text.lower())
#Con count(), cuenta cuantas veces se repetite un caracter
print(text.count('a'))
#Con swapcase() convierte mayusculas a minusculas
print(text.swapcase())
#Con swith() --> startswith() | endswith() devuelve un bool y como atributos va la palabra a checar
print(text.startswith('Yo'))
print(text.endswith('JS'))
#Con replace() --> cambia el atributo por otro (a,b)
print(text.replace('Python', 'JS'))
#Con capitalize() remplaza la primer letra en mayuscula
print(text.capitalize)
#con title() cada palabra la remplaza la primer letra por una mayuscula
print(text.title)
