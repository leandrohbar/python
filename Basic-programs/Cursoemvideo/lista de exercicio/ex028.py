'''Exercício Python 028: Escreva um programa que
faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

import random

num = random.randint(0, 5) # choose a value among the 0 and 5
while True:
    guess = int(input("Digite um valor entre 0 e 5 = ")) # prompt the user the tap a number
    if guess >= 0 and guess <= 5:
        break

print(f'Valores: pc {num}, usuario {guess}')
# verify if the user guessed the same number the pc chose
if guess == num:
    print("Você acertou o número!")
else:
    print("Você errou o numero!")