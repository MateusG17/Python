def classificacaoProduto(numCodigo):
    if numCodigo == 1:
        print('Classificação: Alimento não perecível')
    elif 2 <= numCodigo <= 4:
        print('Classificação: Alimento perecível')
    elif 5 <= numCodigo <= 6:
        print('Classificação: Vestuário')
    elif numCodigo <= 7:
        print('Classificação: Higiene Pessoal')
    elif 8 <= numCodigo <= 15:
        print('Classificação: Limpeza e Utensílios Doméstico')
    else:
        print('Código Invalido')


NumDoCodigo = int(input('Digite o Código: '))

classificacaoProduto(NumDoCodigo)
