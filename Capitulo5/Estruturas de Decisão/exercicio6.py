def ParOuImpar(num):
    if num % 2 != 0:
        print(f'O {num} é impar')
    else:
        print(f'O {num} é par')


num = int(input('Escreva um numero: '))

ParOuImpar(num)