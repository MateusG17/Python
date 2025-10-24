contador = 0
print("Digite 5 números ínteiros. ")

for i in range (1, 6):
    num = int(input(f"Digite {i}° número: "))

    if num % 3 == 0:
        contador += 1

    print(f"Quantidade de números divisíveis por 3: {contador}")

