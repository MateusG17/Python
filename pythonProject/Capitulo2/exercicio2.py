precoCapa = 24.95
descontoLivraria = precoCapa * 0.40
precoCapaLivraria = precoCapa - descontoLivraria

fretePrimeiroExemplar = 3.00
freteRestanteExemplar = 0.75

custoAtacadoPrimeiroExemplar = precoCapaLivraria + fretePrimeiroExemplar
custoAtacado = custoAtacadoPrimeiroExemplar + ((precoCapaLivraria + freteRestanteExemplar) * 59)

print('o custo total de atacado de 60 copias e de: ', custoAtacado)








