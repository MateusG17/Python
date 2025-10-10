def verificaIdade(idade1 , idade2, idade3, idade4, idade5):
    contaIdade = 0

    if(idade1 == 21):
        contaIdade += 1

    if(idade2 == 21):
        contaIdade += 1

    if(idade3 == 21):
        contaIdade += 1

    if(idade4 == 21):
        contaIdade += 1

    if(idade5 == 21):
        contaIdade += 1

        print(f'O número de idades iguais a 21 é: {contaIdade}')

def main():
    idade1 = int(input('Digite sua Idade: '))
    idade2 = int(input('Digite sua Idade: '))
    idade3 = int(input('Digite sua Idade: '))
    idade4 = int(input('Digite sua Idade: '))
    idade5 = int(input('Digite sua Idade: '))

    verificaIdade(idade1, idade2, idade3, idade4, idade5)
if __name__ == '__main__':
    main()