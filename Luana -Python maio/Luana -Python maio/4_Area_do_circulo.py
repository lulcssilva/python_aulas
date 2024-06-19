#=========================================================
#Autor: Luana
#Data: 28/05/2024
#Versão: 1.0
#Descrição:  Faça um algoritmo que receba o raio em metros de um
#            circulo e apresente a sua área
#       -------------------------------------------------
#       Exemplo de execução?
#       insira o raio em metros: 5
#       Área do circulo 78.5m²
#       a = área
#       pi = 3.14
#       r = raio
#       a = pi * r²
#=========================================================
#Variáveis
area = 0
raio = 0
pi = 3.14
#entrada
raio = float(input('Digite o valor do raio em metros'))
#processamento
area = pi * (raio**2)
#saida
print('a área do circulo em metros é: ', area)
