def divisaoCincoTres(num):
    if num % 5 == 0 and num % 3 == 0:
        print(f'O {num} pode ser dividido por 5 e 3')
    else:
        print(f'O {num} nâo pode ser dividido por 5 e 3')

num = int(input(f'Digite um numero: '))

divisaoCincoTres(num)