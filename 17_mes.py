'''
Autor: Luana 
Data: 17/06/2024
Versão: 1.0
Descrição:Faça um programa que receba o número do mês e apresente ele por extenso:
!sem utilizar conficional!
if == 0
    print('mes não existe')
else if mes == 1 
    print('Janeiro')
'''
meses = ['','Janeiro', 'Fevereiro', 'Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

while True:
    nr_mes = 0
    nr_mes = int(input('Digite o número do mês'))
    print(meses[nr_mes]) 
    
    continuar = input('Digite S para sair ou C para Continuar')
    if continuar == 'S':
        break