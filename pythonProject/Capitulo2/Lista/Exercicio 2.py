# Aplicativo para separar dígitos de um número 5 dígitos

# Solicita o número as usuário
num = int(input("Digite um número de 5 dígitos "))

# Extrai cada dígito usando operações matemáticas
    num1 = num // 10000
    num2 = (num % 10000) // 1000
    num3 = (num % 1000) // 100
    num4 = (num % 100) // 10
    num5 = num % 10

 # Imprime os dígitos um em baixo do outro
print(" ", num1)
print(" ", num2)
print(" ", num3)
print(" ", num4)
print(" ", num5)

