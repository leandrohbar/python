'''Exercício Python 027: Faça um programa que leia o nome completo
de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

Ex: Ana Maria de Souza (primeiro = Ana; último = Souza.'''

nome = str(input('Digite um nome completo = '))
# split the name into a list of names to better index the names
nomes = nome.split()

# print the first and the last name
print(f'O primeiro nome é = {nomes[0]}, o ultimo nome é = {nomes[len(nomes) - 1]}')