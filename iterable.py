# con el ciclo for, reserva el espacio en memoria desde el inicio
for i in range(1,20):
    print(i)
#Mientras que el iterador es manual, ya que se controla la forma en que se ejecuta el proceso y no ocupa tanta memoria
my_iter = iter(range(1,11))
print(my_iter)
print(next(my_iter))
print(next(my_iter))