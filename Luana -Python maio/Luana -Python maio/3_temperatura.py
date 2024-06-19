#=========================================================
#Autor: Luana
#Data: 28/05/2024
#Versão: 1.0
#Descrição:  Faça um algoritmo que receba a temperatura em ºC
#            e converta para ºF e k
#              -------------------------------------
#              Exemplo de execução:
#              Insira a temperatura em Celsius: 0ºC
#              Fahrenheit: 32ºF
#              Kelvin: 273,15K
#              -------------------------------------
#=========================================================
#variaveis
celsius = 0 #temperatura em celsius inseridas pelo usuário
fahrenheit = 0 #temperatura em Fahrenheit inserida pelo usuário
kelvin = 0 #temperatura em kelvin inserida pelo usuário
#entrada
celsius = float(input('insira a temperatura em celsius: '))
#processamento
fahrenheit = (celsius * (9/5)) + 32
kelvin = celsius + 273.15
#saida
print(celsius, 'ºC equivalem ', fahrenheit, 'ºF')
print(celsius, 'ºC equivalem ', kelvin, 'K')
#=========================================================