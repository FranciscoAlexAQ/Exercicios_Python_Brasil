'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

letra = str(input('Digite uma letra: ')).lower()

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f'{letra} é vogal!')
else:
    print(f'{letra} não é vogal!')
