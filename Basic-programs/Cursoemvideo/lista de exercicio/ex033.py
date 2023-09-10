import numpy as np
num = [int(input(f'Digite o {i}º número: ')) for i in range(1, 4)]
maior = max(num)
menor = min(num)
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')