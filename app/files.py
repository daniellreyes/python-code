#Con el metodo -> Open, puede cargar en una variable todo un archivo
file = open('./text.txt')
#Tambien se puede abrir un archivo línea a línea
print(file.readlines())
#Hay que tener en cuenta que si el metodo open ocupa espacio en memoria, por lo que se puede indicar cuando parar
file.close()
#Tambien se puede declarar un ciclo for
for line in file:
    print(line)

with open('./text.txt') as file:
    for line in file:
        print(line)