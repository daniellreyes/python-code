#con el metodo ->open, solo tiene permisos de escritura. Cuando se le agrega el ->w SOLO escribe
#con el -> r+ hace read y write
with open('./text.txt', 'r+') as file:
    for line in file:
        print(line)
    file.write('\nescribiendo mas cosas\n')
    file.write('otra linea\n')
    file.write('ultima linea\n')