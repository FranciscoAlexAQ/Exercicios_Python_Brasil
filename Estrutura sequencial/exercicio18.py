'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de 
um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo 
usando este link (em minutos).
'''

tamanho = float(input('Digite o tamanho do arquivo em MB: '))
velocidade = float(input('Digite a velocidade da Internet: '))

tempo_download_minutos = ((tamanho * 8) / velocidade) / 60

print(f'O arquivo será baixado em {tempo_download_minutos:.0f} minutos')
