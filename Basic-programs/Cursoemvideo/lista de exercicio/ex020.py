import random
alunos = []

for i in range(4):
    alunos.append(str(input('Digite o nome do aluno = ')))

random.shuffle(alunos)
print(alunos)
