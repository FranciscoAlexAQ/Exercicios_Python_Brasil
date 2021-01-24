'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% 
Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''

salario = float(input('Digite o salário: '))
aumento = float(input('Digite o percentual de aumento: '))

if salario <= 280:
    total = salario * 20 / 100
elif 280 < salario < 700:
    total = salario * 15 / 100
elif 700 <= salario < 1500:
    total = salario * 10 / 100
else:
    total = salario * 5 / 100

print(30 * '=')

print(f'Salário antes do reajuste: R${salario:,.2f}')
print(f'Percentual de aumento: {aumento:.2f}%')
print(f'Valor do aumento: R${total:,.2f}')
print(f'Novo salário após o aumento: R${(salario + total):,.2f}')
