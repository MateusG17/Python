def validaIdade(idade):
    if(idade >= 18):
        print("Você é maior de idade ")
    else:
        print("Você é menor de idade ")

idade = int(input("Qual a sua idade "))

validaIdade(idade)