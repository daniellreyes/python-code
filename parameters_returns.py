#Introduciendo 3 parametros
def find_volume(height, width, depth):
    return height * width * depth

result = find_volume(3,3,3)
print(result)

#introduciendo 3 parametros y devolviendo 3 returns
def find_volume(height=2, width=1, depth=5):
    return height * width * depth, 'soyDaniel', depth

result, text, depeth = find_volume(width=3)
print(result)
print(text)
print(depeth)
print(result, text, depeth)