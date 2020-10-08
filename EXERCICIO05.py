"""
Crie um programa que leia a altura de 10 pessoas. Ao final o programa deve informar o total de pessoas cadastradas, a quantidade de pessoas com altura inferior a 1,60 metros; a quantidade de pessoas com altura entre 1,60 metros e 1,80 metros e a quantidade de pessoas com altura superior a 1,80 metros.
"""

cadastros = inferior = entre = superior = 0

for c in range(10):

    altura = float(input('altura: '))

    if altura < 1.6:

        inferior += 1

    elif 1.8 >= altura >= 1.6:

        entre += 1

    else:

        superior += 1

print(f'''
Foram cadastradas 10 pessoas.
Pessoas com altura menor de 1,60m: {inferior}
Pessoas com altura entre 1,60m e 1,80m : {entre}
Pessoas com altura superior a 1,80m: {superior}''')