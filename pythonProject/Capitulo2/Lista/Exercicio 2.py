# Aplicativo para separar dígitos de um número 5 dígitos

# Solicita o número as usuário
num = int(input("Digite um número de 5 dígitos "))

# Verifica se o número tem 5 dìgitos
if 10000 <= num <= 99999:
    # Extrai cada dígito usando operações matemáticas
    digito1 = num // 10000
    digito2 = (num % 10000) // 1000
    digito3 = (num % 1000) // 100
    digito4 = (num % 100) // 10
    digito5 = num % 10

    # Imprime os dígitos separados por três espaços
    print(f"{digito1} {digito2} {digito3} {digito4} {digito5}")
else:
    print("Por favor, digite um número de exatamente 5 dígitos")