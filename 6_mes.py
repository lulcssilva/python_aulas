'''
Autor: Luana
Data 28/05/2024
versão 1.0
descrição:
            Mês aniversário
            Escreva um algoritmo para exibir o nome do mês por extenso de acordo com o número que o representa
            1       Janeiro
            2       Fevereiro
            3       Março
            4       Abril
            5       Maio
            6       Junho
            7       Julho
            8       Agosto
            9       Setembro
            10      Outubro
            11      Novembro
            12      Dezembro

'''
nr_mes = ''
mes = ''
nr_mes = input('insira o número do mês:')
if nr_mes == '1':
    mes = 'Janeiro'
elif nr_mes == '2':
     mes = 'Fevereiro'
elif nr_mes == '3':
     mes = 'Março'
elif nr_mes =='4':
     mes = 'Abril'
elif nr_mes == '5':
     mes = 'Maio'
elif nr_mes == '6':
     mes = 'Junho'
elif nr_mes == '7':
     mes = 'Julho'
elif nr_mes == '8':
     mes = 'Agosto'
elif nr_mes == '9':
     mes = 'Setembro'
elif nr_mes == '10':
     mes = 'Outubro'
elif nr_mes == '11':
     mes = 'Novembro'
elif nr_mes == '12':
     mes = 'Dezembro'
else:
    mes ='Digite um valor válido'
print( mes)