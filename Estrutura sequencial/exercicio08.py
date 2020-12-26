'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
'''

ganho_por_hora = float(input('Quanto você ganha por hora: '))
horas_trabalhadas = int(input('Digite o número de horas trabalhadas: '))

print(f'Seu salário nesse mês é de R${ganho_por_hora *horas_trabalhadas:,.2f}')
