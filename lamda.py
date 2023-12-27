def increment(x):
    return x+1

result = increment(10)
print(result)
#Una funcion lambda tienen una sintaxis mas corta que una normal
increment_v2 = lambda x : x+1
result = increment_v2(20)
print(result)
#Lambda function para la suma de dos numeros
sum_num1_num2 = lambda num1, numb2 : num1+numb2
result = sum_num1_num2(4,2)
print(result)
#La f es para dar formato a la cadena de texto
full_name = lambda first_name, last_name : f'Full name is {first_name.title()} {last_name.title()}'
text = full_name('daNiel', 'reyes')
print(text)