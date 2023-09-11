'''Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
import numpy as np
num = [int(input(f'Digite o {i}º número: ')) for i in range(1, 4)]
print(f'O maior número é {max(num)}')
print(f'O menor número é {min(num)}')