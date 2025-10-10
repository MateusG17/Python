def soma(num1, num2, num3, num4):
    total = 0

    if(num1 % 2 == 0):
        total += num1
    if (num2 % 2 == 0):
        total += num2
    if (num3% 2 == 0):
        total += num3
    if (num4 % 2 == 0):
        total += num4

    return total

def contaPares(num1, num2, num3, num4):
    total = 0

    if(num1 % 2 == 0):
        total += 1
    if (num2 % 2 == 0):
        total += 1
    if (num3 % 2 == 0):
        total += 1
    if (num4 % 2 == 0):
        total += 1

    return total

def main():
    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite um numero: '))
    num3 = int(input('Digite um numero: '))
    num4 = int(input('Digite um numero: '))

    totalSoma = soma(num1, num2, num3, num4)
    totalPares = contaPares(num1, num2, num3, num4)
    media = totalSoma / totalPares
    print(f'A soma dos numeros é: {totalSoma}')
    print(f'A soma dos numeros é: {media}')

if __name__ == '__main__':
    main()