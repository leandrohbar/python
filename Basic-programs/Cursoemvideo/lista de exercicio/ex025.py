'''Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''

nome = str(input('Digite o nome da pessoa = '))

#verifica se tem o nome silva no nome
if nome.upper().count('SILVA') > 0:
    print('Tem o nome SILVA!')
else:
    print('NÃO tem o nome SILVA!')

