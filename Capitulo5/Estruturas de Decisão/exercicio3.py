def algoritmoNumeros(algoritmo1, algoritmo2, algoritmo3):
    if (algoritmo1 >= algoritmo2 >= algoritmo3):
        print("O", algoritmo1 , "é o maior ")
    if (algoritmo2 >= algoritmo3 >= algoritmo1):
        print("O", algoritmo2 , "é o maior ")
    if (algoritmo3 >= algoritmo2 >= algoritmo1):
        print("O", algoritmo3 , "é o maior ")

algoritmo1 = int(input("Os numeros são" ))
algoritmo2 = int(input("Os numeros são" ))
algoritmo3 = int(input("Os numeros são" ))

algoritmoNumeros(algoritmo1, algoritmo2, algoritmo3)