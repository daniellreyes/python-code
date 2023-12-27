# Los sets tienen como estructura -> set_variable = set{'set1', 'set2', ... 'setn'}

set_countries = {'mexico', 'usa', 'austria'}
print(set_countries)

set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)

set_types = {1, 'daniell', False, 12.12}
print(set_types)

#En este caso, solo imprimira una 'o' y devolvera en desorden!
set_from_string = set('hoola')
print(set_from_string)
#tambien se pueden usar tuplas con los sets
set_from_tupples = set(('abc', 'tuf', 'as', 'tuf'))
print(set_from_tupples)
#al transformarlo con set, funciona con los principios de conjuntos; no se permiten elementos repetidos
numbers = [1,2,3,4,5,6]
set_numbers = set(numbers)
print(set_numbers)