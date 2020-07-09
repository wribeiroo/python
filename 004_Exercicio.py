
# VALIDAÇÕES BÁSICAS

valor = input('Digite algo: ')
print('')
print('O valor digitado foi {}.'.format(valor))
print('')
print('O tipo primitivo do valor é {}.'.format(type(valor)))
print('Só tem espaços? {}'.format(valor.isspace()))
print('É um número? {}'.format(valor.isnumeric()))
print('É alfabético? {}'.format(valor.isalpha()))
print('É alfanumérico? {}'.format(valor.isalnum()))
print('Está em maiúsculas? {}'.format(valor.isupper()))
print('Está em minúsculas? {}'.format(valor.islower()))
print('Está capitalizada? {}'.format(valor.istitle()))


