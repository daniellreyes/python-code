#Definiendo funciones de manera normal
def increment(x):
    return x+1

increment_lambda = lambda x: x+1

def high_ord_func(x, func):
    return x + func(x)

high_ord_func_v2 = lambda x, func : x + func(x)

result1 = high_ord_func(2, increment)
print(result1)
#aqui, x trae el valor de 4
result2 = high_ord_func_v2(4, increment_lambda)
print(result2)