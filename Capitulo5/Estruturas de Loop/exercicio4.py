maior = 0
menor = 0
for i in range (0, 10):
 num = int(input('Digite um numero: '))

 if i == 0:
     maior = num
     menor = num
 if num > maior:
     maior = num
 elif num < menor:
     menor = num

print(f'O maior numero é: {maior}')
print(f'O menor numero é: {menor}')

