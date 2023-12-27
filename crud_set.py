# Haciendo uso de un CRUD -> Create Remove, Update & Delete
set_countries = {'mexico', 'usa', 'austria'}

size = len(set_countries)
print(size)

print('col' in set_countries)
print('mexico' in set_countries)

# C-> Create | add
set_countries.add('col')
print(set_countries)
#U -> Update 
set_countries.update({'canada', 'nueva zelanda', 'mexico'})
print(set_countries)

#R -> Remove | hay dos formas con remove & discard. Discard sino encuentra, sigue proceso.
set_countries.remove('usa')
print(set_countries)
set_countries.discard('EE.UU')
print(set_countries)
#R -> RemoveEverything con Clear | Devuelve un conjunto en vacio
set_countries.clear()
print(set_countries)

