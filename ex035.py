"""Desenvolva um programa que leia o comprimento de três retas e diga ao utilizador se elas podem ou nao formar
um triângulo"""
from time import sleep

print('\33[0:36m:+=+=\33[0:0m' * 18)
print('                                  \33[0:31mAnalisador de Triângulos\33[0:0:m             ')
print('\33[0:36m:+=+=\33[0:0m' * 18)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print('\33[0:33mCARREGANDO INFORMAÇÃO\33[0:0m...')
sleep(3)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \33[1:32m PODEM FORMAR \33[0:0m um Triangulo')
else:
    print('Os segmentos acima \33[0:31mNÃO PODEM FORMAR \33[0:0m um triângulo')
