'''
Faça um Programa que leia três números e mostre o maior e o menor deles.
'''


n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))

if n1 >= n2 and n1 >= n3 and n2 >= n3:
    print(f'Maior: {n1} Menor: {n3}') 
elif n1 >= n2 and n1 >= n3 and n2 <= n3:
    print(f'Maior: {n1} Menor: {n2}') 
elif n2 >= n1 and n2 >= n3 and n1 >= n3:
    print(f'Maior: {n2} Menor: {n3}')
elif n2 >= n1 and n2 >= n3 and n1 <= n3:
    print(f'Maior: {n2} Menor: {n1}') 
elif n3 >= n1 and n3 >= n2 and n1 >= n2:
    print(f'Maior: {n3} Menor: {n2}')
elif n3 >= n1 and n3 >= n2 and n1 <= n2:
    print(f'Maior: {n3} Menor: {n1}')
