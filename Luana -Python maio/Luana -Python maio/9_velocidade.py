'''
Autor: Luana 
Data 06/06/2024
versão 1.0
descrição: "multa velocidade"
Escreva um programa que leia a velocidade máxima permitida em uma avenida e a velocidade com que o motorista estava dirigindo nela e calcule a 
multa que a pessoa vai receber de acordo com a tabela abaixo:

Velocidade ultrapassada       valor multa
    até 10km/h                R$ 50,00
    11 a 30km/h               R$ 100,00
    mais de 31km/h            R$ 200,00
'''
limiteVelocidade = 0
velocidadeMotorista = 0
diferencaVelocidade = 0
valorMulta = ''

limiteVelocidade = int(input('Qual a velocidade da permitida na pista?'))
velocidadeMotorista = int(input('Qual a velocidade do carro?'))
diferencaVelocidade = velocidadeMotorista - limiteVelocidade

if (diferencaVelocidade > 0 and diferencaVelocidade <=10):
    valorMulta = 'R$ 50,00'
elif (diferencaVelocidade >= 11 and diferencaVelocidade<=30):
    valorMulta = 'R$100'
elif (diferencaVelocidade>=31):
    valorMulta = '200'
else:
    valorMulta = 'R$0,00'
print (valorMulta)