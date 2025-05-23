# Aplicativo com valor fixo de pi

# Define o raio ao usuário
PI = 3.14159

# Solicita o raio ao usuário
raio = int(input("Digite o raio do círculo (número inteiro): "))

# Calcule as propriedades
diametro = 2 * raio
circunferencia = 2 * PI * raio
area = PI * (raio ** 2)

# Exibe os resultados
print("Diametro: ", diametro)
print("Circunferencia: ", circunferencia)
print("Área: ", area)