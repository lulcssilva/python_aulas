'''
Autor: Luana 
Data 06/06/2024
versão 1.0
descrição: 'Tipo de triângulo'
Faça um programa que receba 3 valores e verifique se eles podem representar os lados em um triângulo:
1 - Triângulo escaleno: triângulo que possui todos os lados com medidas diferentes.
2 - Triângulo isósceles: triângulo que possui dois lados com medidas iguais.
3 - Triângulo equilátero: triângulo que possui todos os lados com medidas iguais.
Lembrando que a soma das medidas de dois lados de um triângulo é sempre maior que a medida do terceiro lado 
'''
ladoA = 0
ladoB = 0
ladoC = 0
tipo_triangulo = 0
# CTRL= ALT +SHIFT+(direcionais up ou down)
ladoA = int(input('Digite o valor do lado A'))
ladoB = int(input('Digite o valor do lado B'))
ladoC = int(input('Digite o valor do lado C'))

if ((ladoA + ladoB) > (ladoC) and 
    (ladoA + ladoC) > (ladoB) and
    (ladoB + ladoC) > (ladoA) and 
    ladoA > 0 and ladoB > 0 and ladoC > 0):
    print ('Triângulo válido')
    if(ladoA != ladoB != ladoC):
        tipo_triangulo = 'Triângulo escaleno: triângulo que possui todos os lados com medidas diferentes'
    if(ladoA == ladoB != ladoC) or (ladoA != ladoB == ladoC) or (ladoA == ladoC != ladoB) or (ladoA != ladoC ==ladoB):
        tipo_triangulo = 'Triângulo isósceles: triângulo que possui dois lados com medidas iguais.'
    if(ladoA == ladoB == ladoC):
        tipo_triangulo = 'Triângulo equilátero: triângulo que possui todos os lados com medidas iguais.'   

else:
    print('Triângulo nãoexiste')
print(tipo_triangulo)






