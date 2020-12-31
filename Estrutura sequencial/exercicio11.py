'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
'''

número1 = int(input('Digite um número inteiro: '))
número2 = int(input('Digite outro número inteiro: '))
número3 = float(input('Digite um número decimal: '))

print(f'{(número1 * 2) * (número2 / 2)}')
print(f'{(número1 * 3) + número3}')
print(f'{número3 ** 3}')
