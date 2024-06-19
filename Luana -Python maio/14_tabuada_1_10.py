'''
Autor: Luana 
Data: 13/06/2024
Versão: 1.0
Algoritmo: Tabuada 1 ao 10
Descrição: Faça um programa que apresente a tabuada do 1 ao 10
'''
#===========================================================
#variáveis
numero = 0
multiplicador = 0
resultado = 0

#Entrada
print('============================================')    
for multiplicador in range(11): #0 -> 10
    for numero in range(11):
        resultado = numero * multiplicador
        print(multiplicador, 'x', numero, '=', resultado)
    print('============================================')    

#===========================================================