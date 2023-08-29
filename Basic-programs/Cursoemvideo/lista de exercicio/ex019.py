import random
aluno1 = input('Digite o nome do aluno = ')
aluno2 = input('Digite o nome do aluno = ')
aluno3 = input('Digite o nome do aluno = ')
aluno4 = input('Digite o nome do aluno = ')

alunos = [aluno4, aluno3, aluno1, aluno2]
print(f'O aluno escolhido é = {random.choice(alunos)}')
