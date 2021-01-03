'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no 
mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos 
dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato (5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

ganho = float(input('Digite o quanto você ganha por hora: '))
horas = int(input('Digite o número de horas trabalhadas no mês: '))

salário_bruto = ganho * horas 
pago_INSS = salário_bruto * 8 / 100
pago_sindicato = salário_bruto * 5 / 100
pago_impostoRenda = salário_bruto * 11 / 100 

print(30 * '-')

print(f'+ Salário Bruto: R${salário_bruto:,.2f}')
print(f'- IR (11%) : R${pago_impostoRenda:,.2f}')
print(f'- INSS (8%) : R${pago_INSS:,.2f}')
print(f'- Sindicato (5%) : R${pago_sindicato}')
print(f'= Salário Líquedo : R${salário_bruto - (pago_sindicato + pago_INSS + pago_impostoRenda):,.2f}')
