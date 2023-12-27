set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}
#Operador unión -> Hay dos formas de declarar la unión, con .union y '|'
set_union_a_b = set_a.union(set_b)
print(set_union_a_b)
print(set_a | set_b)
#Operador interseccion -> de igual forma hay dos formas con .intersection y '&'
set_intersection_a_b = set_a.intersection(set_b)
print(set_intersection_a_b)
print(set_a & set_b)
#Operador diferencia -> de igual forma hay dos formas con .difference y '-'
set_diference_a_b = set_a.difference(set_b)
print(set_diference_a_b)
print(set_a - set_b)
#Operador 'Symmetric Difference' -> es basicamente la unión pero sin la intersección de los conjuntos
# hay dos formas, .symmetric difference y -^-
set_symmetricdiffence_a_b = set_a.symmetric_difference(set_b)
print(set_symmetricdiffence_a_b)
print(set_a ^ set_b)