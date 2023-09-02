"""Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e
mostre na tela cada um dos dígitos separados."""

num = int(input('Digite um numero entre 0 e 9999 = '))

# verifica se o valor esta dentro do range
while num < 0 or num > 9999:
    num = int(input('Valor inválido!\nDigite um numero entre 0 e 9999 = '))

# converte para string e print cada digito do numero.
for i in range(len(str(num))):
    print(str(num)[i], end=' ')
