def consumoEnergia(opcao):
    match opcao:
     case ('A') :
        print(f'Muito Eficiente')
     case ('B') :
        print(f'Eficiente')
     case ('C') :
        print(f'Pouco Eficiente')
     case ('D') :
        print(f'Ineficiente')
     case _ :
         print(f'Classificação {opcao} não foi encontrado')





def main():
    print("Digite a Letra de Classificação da sua Geladeira:")
    opcao = input()

    consumoEnergia(opcao)
if __name__== '__main__':
    main()







