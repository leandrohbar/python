"""Exercício Python 024: Crie um programa que leia o nome de uma cidade
diga se ela começa ou não com o nome "SANTO"."""

cidade = str(input('Digite o nome de uma cidade = ')).strip()

nomes = cidade.split() # divide os nomes da cidade em lista de string

# verifica se começa com santo ou nao
if nomes[0].upper() == 'SANTO':
    print('O nome da cidade começa com SANTO!')
else:
    print('O nome da cidade NÃO começa com SANTO!')