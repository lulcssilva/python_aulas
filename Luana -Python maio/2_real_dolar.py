#=========================================================
#Autor: Luana
#Data: 28/05/2024
#Versão: 1.0
#Descrição: Faça um algoritmo que um valor na moeda real (R$),
#           a cotação da conversão REAL para DÓLAR, e apresente
#           a quantidade desse valor em dólar ($)
#           ------------------------------------------
#           Exemplo de execução
#           Insira o valor em real: 5000
#           Insira cotação do dia: 5
#           R$5000,00 equivalem $1000,00
#           ----------------------------------------
#
#=========================================================
#variáveis 
real = 0 #recebe o valor em reais
cotacao = 0 #valor da cotação 1dolar x reais
dolar = 0 #valor convertido real para dólar
#entrada 
print('###############################')
#necessario fazer o casting(conversão de tipos de dados) Float- string
real = float(input('insira o valor em reais?')) 
cotacao = float(input('insira o valor da cotação'))
#processamento
dolar = real/cotacao
#saida
print('R$',real,'equivalem','$', dolar)
print('####################################')
#=========================================================
