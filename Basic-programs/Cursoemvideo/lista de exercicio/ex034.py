'''Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('Qual é o salário do funcionário? R$'))
if salario > 1250:
    print(f'Quem ganhava R${salario:.2f} passa a ganhar \033[4;33mR${salario * 1.10:.2f} agora.\033[m')
else:
    print(f'\033[4;34;47mQuem ganhava R${salario:.2f} passa a ganhar R${salario * 1.15:.2f} agora.\033[m')