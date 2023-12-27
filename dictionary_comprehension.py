
#Creacion de un diccionario -> clave valor llenandolo con un array
my_dictionary = {}
for i in range(1, 3):
    my_dictionary[i] = i * 5
print(my_dictionary)

#Uso del dictionary comprehension. La estructura es {key:value for var in iterable}
my_dictionary2 = {i: i*5 for i in range(1, 3)}
print(my_dictionary2)

#Creacion de un diccionario -> clave valor llenandolo con un array
my_dictionary = {}
for i in range(1, 3):
    my_dictionary[i] = i * 5
print(my_dictionary)

#Uso del dictionary comprehension. La estructura es {key:value for var in iterable}
my_dictionary2 = {i: i*5 for i in range(1, 3)}
print(my_dictionary2)

#Uniendo dos listas para crear un diccionario
dictionary_names = ['daniel', 'raul', 'Nat']
dictionary_ages = [12, 24, 25]
#Forma 'tradicional'
print(list(zip(dictionary_names, dictionary_ages)))
#Utilizando dictionary comprehension || el metodo zip transforma a la apariencia clave valor
dictionary_names_age = {dictionary_name : dictionary_age for (dictionary_name, dictionary_age) in zip(dictionary_names, dictionary_ages)}
print(dictionary_names_age)
