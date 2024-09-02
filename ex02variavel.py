algo = input('Digite algo: ') # todo retorno de input é uma string

print('O tipo primitivo é ', type(algo))
print('Só tem espaços?', algo.isspace())
print('É um número?', algo.isnumeric())
print('É alfabético?', algo.isalpha())
print('É alfanumérico?', algo.isalnum())
print('Está em maiúsculas?', algo.isupper())
print('Está em minúsculas?', algo.islower())
print('Está capitalizada?', algo.istitle())
