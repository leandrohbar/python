'''Exercício Python 029: Escreva um programa que leia
a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

velocidade = float(input('Digite a velocidade do carro = '))

if velocidade >= 80:
    print(f'Você ultrapassou do limite de velocidade em {velocidade - 80:.1f}Km e sera multado com o valor de R${(velocidade - 80) * 7:.2f}!')
else:
    print('Você não ultrapassou o limite de velocidade!')