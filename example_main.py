# strings y concatenacion
my_name1 = "Daniel"
my_name2 = 'Reyes'

print("Yo soy ", my_name1, " y mi apellido es ", my_name2)
print(type(my_name1))

# Enteros || Integers

my_edge = 24
a = 2.3
print(my_edge)
print("Esta es mi edad: ", my_edge)
print(type(a))

# Booleanos || con True or False!
is_single = False
is_married = True
print("Estoy casado?", is_single)

#Para poder leer datos del usuario || -> input
#a = input("Como te llamos?")
#print(a)

#b=print(b, input("Como te llamas?"))

#IMPORTANTE -> Python es de alto nivel, interpretado (se ejecuta linea por linea) y tipeado dinamico
#Por lo que, puedes agregar el tipo de dato con la siguiente sintaxis

#name: str = 'Daniel'
#age: int = 24
#is_married: bool = False

#Casteo! || str(age) -> convierte un int/float a str
age = 14
print("Mi edad es de " + str(age))

#Listas || List []

numbers = [1, "Golaaaa", 3, 4, True]
print(numbers)
print(type(numbers))
#Pueden ser modificadas, cada elemento esta separado por una coma, puede contener todo tipo de datos


tasks = ['wake up', 'drink water']
print(tasks)
print(type(tasks))