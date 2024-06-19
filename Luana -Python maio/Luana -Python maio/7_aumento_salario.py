'''
Autor: Luana 
data: 04/06/2024
descrição: algoritmo de salário
    Faça um programa que reveba o salário de um funcionário, calcule e mostre o novo salário, sabendo que:
    Salário < R$1000,00 aumento de 25%
    Salário >= R$1000,00 e <R$ 2000,00 aumento de 15%
    salário >= 2000,00 aumento de 10%
'''
salario = 0 
salario_aumento = 0
salario = float(input('Digite o seu salário e descubra qual será seu novo salário após o aumento!'))
if salario < 1000:
    salario_aumento = salario*1.25
    salario_aumento = round(salario_aumento)
    print('Você terá um aumento de 25% e seu novo salário será: ', salario_aumento)
elif salario >= 1000 and salario < 2000:
     salario_aumento = salario *1.15
     salario_aumento = round(salario_aumento)
     print('Você terá um aumento de 15% e seu novo salário será: ', salario_aumento)
else:
    salario_aumento = salario *1.10
    salario_aumento = round(salario_aumento)
    print('Você terá um aumento de 10% e seu novo salário será: ',salario_aumento)

    