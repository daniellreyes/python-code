items = [
    {
        'product': 'camisa',
        'price': 20
    },
    {
        'product': 'pantalones',
        'price': 30
    },
    {
        'product': 'corbata',
        'price': 5.99
    }
]

prices = list(map(lambda item : item['price'], items))
print(prices)
#Como no se puede hacer la lambda function (en un solo renglon), se hace uso de una funcion
def add_taxes(item):
    #WARNING! al estar iterando, se esta modificando el array originial (los diccionarios especiificamente)
    #Por lo que lo ideal es crear una copia y trabajar con esa misma.
    new_item = item.copy()
    new_item['taxes'] = item['price'] * 0.19
    return new_item
#retorna el diccionario items pero con la clave -> taxes y el valor correspondiente
new_items = list(map(add_taxes, items))
print(new_items)
print(items)