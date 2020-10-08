"""Faça um programa que dado o valor da temperatura em graus FARENHEIT, calcular e escrever o valor da temperatura em
graus CELSIUS. Fórmula: C = 5/9 * (F - 32) """
fah = int(input('Informe a temperatura em Celsius: '))
celsius = (fah - 32) * 5 / 9
print('{:.0f}ºC corresponde a {:.0f}ªF'.format(fah, celsius))