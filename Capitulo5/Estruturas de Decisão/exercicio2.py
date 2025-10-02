def numeroNum(numero):
    if(numero > 0):
        elevado = numero ** 2
        print(elevado)

    if(numero < 0):
        print("O seu numero é negativo ")

numero = int(input("Digite seu numero "))

numeroNum(numero)