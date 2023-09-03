'''Exercício Python 026: Faça um programa que leia uma frase pelo
teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

frase = str(input('Digite uma frase = ')).strip()

print(f'A letra \"A\" aparece = {frase.upper().count("A")} vezes!')
print(f'A letra \"A\" aparece a 1ª vez no posição = {frase.upper().find("A") + 1}')
print(f'A letra \"A\" aparece pela ultima vez no posição = {frase.upper().rfind("A") + 1}')