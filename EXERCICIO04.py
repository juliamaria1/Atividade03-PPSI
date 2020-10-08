"""
Faça um programa que leia dois números e mostre qual o maior dos dois. O programa deve informar caso sejam iguais.
"""
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

if n1 > n2:
    print('{} é o maior número.'.format(n1))
if n2 > n1:
    print('{} é o maior número.'.format(n2))
if n1 == n2:
    print('Os números são iguais.')