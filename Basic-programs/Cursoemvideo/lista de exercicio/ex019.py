import random
aluno1 = str(input('Digite o nome do aluno = '))
aluno2 = str(input('Digite o nome do aluno = '))
aluno3 = str(input('Digite o nome do aluno = '))
aluno4 = str(input('Digite o nome do aluno = '))

alunos = [aluno1, aluno2, aluno3, aluno4]
print(f'O aluno escolhido é = {random.choice(alunos)}')
