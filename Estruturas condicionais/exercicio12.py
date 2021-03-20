'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de 
Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS 
corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido 
corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora 
e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 

Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 
e a quantidade de hora é 220.

        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''

preço = float(input('Quanto você ganha por hora? ').strip())
horas = float(input('Quantas horas você trabalhou? ').strip())

salário_bruto = preço * horas

if salário_bruto >= 0 and salário_bruto <= 900:
    IR = 0
elif salário_bruto > 900 and salário_bruto <= 1500:
    IR = 5 * salário_bruto / 100
elif salário_bruto > 1500 and salário_bruto <= 2500:
    IR = 10 * salário_bruto / 100
elif salário_bruto > 2500:
    IR = 20 * salário_bruto / 100
else:
    IR = 0 

INSS = 10 * salário_bruto / 100
FGTS = 11 * salário_bruto / 100

print(f'''
    Salário Bruto          : R$ {salário_bruto:,.2f}
    (-) IR (5%)            : R$ {IR:>8,.2f}
    (-) INSS (10%)         : R$ {INSS:>8,.2f}
    FGTS (11%)             : R$ {FGTS:>8,.2f}
    Total de descontos     : R$ {(IR + INSS):>8,.2f}
    Salário Líquido        : R$ {(salário_bruto - (IR + INSS)):,.2f}
''')
