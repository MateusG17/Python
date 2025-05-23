# Aplicativo de Operações Aritméticas
# Solicita dois números inteiros e mostra a soma, produto, diferenças e quociente

# Solicita os números ao usuário
num1 = int(input("Digite o primeiro número inteiro "))
num2 = int(input("Digite o segundo número inteiro "))

# Calcula as operações
soma = num1 + num2
produto = num1 * num2
diferença = num1 - num2
quociente = num1 / num2

# Exibe os resultados
print("\nResultados:")
print(f"Soma: {num1} + {num2} = {soma}")
print(f"Produto: {num1} * {num2} = {produto}")
print(f"Diferença: {num1} - {num2} = {diferença}")
print(f"Quociente: {num1} / {num2} = {quociente:2f}")