'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para 
cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam 
R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o 
preço total.
'''

metros_quadrados = float(input('Qual é a área da parede a ser pintada? '))

if metros_quadrados < 3:
    litros = 1
else:
    litros = metros_quadrados / 3

latas = int(litros % 18)
preço = latas * 80 

print(f'Latas necessárias: {latas} Preço R${preço:,.2f}')
