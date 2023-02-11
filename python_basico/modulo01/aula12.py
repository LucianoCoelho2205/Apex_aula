from random import choice

n1 = input('digite o nome: ')
n2 = input('digite o nome: ')
n3 = input('digite o nome: ')
n4 = input('digite o nome: ')
n5 = input('digite o nome: ')
n6 = input('digite o nome: ')
n7 = input('digite o nome: ')

lista = [n1, n2, n3, n4, n5, n6, n7]

sorteando = choice(lista)

print(f'o nome do soteado foi {sorteando}')
