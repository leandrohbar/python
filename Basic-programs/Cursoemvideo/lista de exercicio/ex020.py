import random
alunos = []

for i in range(4):
    alunos.append(input('Digite o nome do aluno = '))

for i in range(4):
    print(f'O aluno é = {random.choices(alunos)}')
