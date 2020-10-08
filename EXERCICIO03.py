"""
Faça um programa para solicitar o nome e as duas notas de um aluno. Calcular sua média e informá-la. Se ela for inferior a 7, escrever "Reprovado”; caso contrário escrever "Aprovado".
"""
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota:  '))

media = (n1 + n2) / 2
print()
print('o aluno obteve a média {}'.format(media))
print()

if media > 7:
    print('O aluno foi aprovado.')
else:
    print('O aluno foi reprovado.')
print()