#=========================================================
#Autor: Luana 
#Data: 24/05/2024
#Versão: 1.0
#Descrição: Faça um algoritmo que receba 5 notas e imprima
#            a média final do aluno
#            ------------------------------------------
#             Exemplo de execução
#             Nota 1: 10
#             Nota 2: 10
#             Nota 3: 10
#             Nota 4: 10
#             Nota 5: 10
#             Média final: 10

#Inicio
#Entrada
nota1 = 7
nota2 = 6
nota3 = 8
nota4 = 9
nota5 = 3
#processamento
Somatoria = nota1 + nota2 + nota3 + nota4 + nota5
print (nota1, ' + ', nota2, ' + ', nota3, ' + ', nota4, ' + ', nota5, ' = ', Somatoria)
resultado = Somatoria / 5 
print (Somatoria, ' / ', 5, ' = ', resultado)

#==========================================================

#Reposta professor
media = (nota1 + nota2 + nota3 + nota4 +nota5) /5
#saida
print ('media do aluno é:', media)
#Fim
#=============================================================
#entrada
#casting = para converter o valor de string inteiro
NotaUm = int(input('Insita a nota 1:'))
NotaDois = int(input('Insita a nota 2:'))
NotaTres = int(input('Insita a nota 3:'))
NotaQuatro = int(input('Insita a nota 4:'))
NotaCinco = int(input('Insita a nota 5:'))
#processamento
media =(notaUm + notaDois + notaTres + notaQuatro + notaCinco)
#saida
print (' A média do aluno é:' media)
#Fim 
