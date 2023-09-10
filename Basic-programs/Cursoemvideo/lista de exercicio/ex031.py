'''Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''

distancia = float(input('Qual é a distância da sua viagem? '))
if (distancia <= 200):
    preco = distancia * 0.50
    print(f'A passagem custará R${preco:.2f}')
else:
    preco = distancia * 0.45
    print(f'A passagem custará R${preco:.2f}')