"""
Elabore um programa para solicitar o nome de uma equipe de futebol, a quantidade de derrotas, empates e vitórias obtidas por ela no campeonato. No futebol, cada vitória vale três pontos e cada empate vale um ponto. Calcular e informar: a quantidade de pontos ganhos, a quantidade de pontos perdidos e o percentual de aproveitamento da equipe.
"""

time = input('Informe um time: ')
pd = int(input('Informe a quantidade de partidas disputadas: '))
v = int(input('Informe quantas vitórias: '))
e = int(input('Informe a quantidade de empates: '))
d = int(input('Informe a quantidade de derrotas: '))

pv = v * 3
pe = e * 1
pg = pv + pe
pc = (pg / (pd*3)) * 100

print('+='*20)

print('O time {} disputou {} partidas, obteve {} vitórias, {} empates e {} derrotas.'.format(time, pd, v, e, d))
print('O time {} ganhou {} pontos.'.format(time, pg))
print('O time {} obteve um aproveitamento de {:.2f}%'.format(time, pc))

print('+='*20)