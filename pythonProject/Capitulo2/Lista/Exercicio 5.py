# Calculadora de Emissão de Carbono por Gasolina

# Fatores de Emissão (fontes: EPA e Carbon Footprint)
FATOR_EMISSAO_GASOLINA = 2.31 # KG CO2 por litro de gasolina
FATOR_CONVERSAO_GALAO_LITRO = 3.78541 # 1 galão = 3.78541 litros

def calcular_emissao_gasolina():
    print("Calculadora de Emissao de Carbono por Gasolina")

# Solicita dados ao usuário
litros_gasolina = float(input("Digite o consumo mensal de gasolina (em litros): "))
meses = int(input("Digite o periodo a calcular (em meses): "))

# Cálculo da emissão
emissao_total = litros_gasolina * FATOR_EMISSAO_GASOLINA * meses

# Exibe resultados
print("Resultado:")
print(f"Emissão total de CO2: {emissao_total:.2f} kg")
print("Equivalências:")
print(f"- {emissao_total/1000:.2f} toneladas de CO2")
print(f"- Equivale ao carbono absorvido por {emissao_total/21:.0f} árvores adultas em um ano")
