km = float(input('Quantos kms você andou com o carro? '))
dias = int(input('Quantos dias você alugou com o carro? '))
print('Valor total = R${:.2f}'.format((km * 0.15) + (dias * 60)))