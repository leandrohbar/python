"""Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome."""

#pede o nome inteiro do usuario
nome = str(input('Digite seu nome completo = '))

#remove os espaços no começo e final
nome = nome.strip()

#print o nome maisculo e minisculo
print(nome.upper())
print(nome.lower())

"""conta quantas letras tem ao todo e no primeiro nome primeiro nome."""
print(len(nome.replace(' ', '')))
nomeSeparado = nome.split()
print(len(nomeSeparado[0]))
