#Faça um programa que preencha por leitura um vetor de 10 posições, e conta quantos valores diferentes existem no vetor.
print("---------------------------------")
def contar_valores_diferentes(vetor):
    valores_diferentes = set(vetor)  # Usando um conjunto para armazenar valores únicos
    quantidade_diferentes = len(valores_diferentes)
    return quantidade_diferentes

vetor = []

for i in range(10):
    valor = int(input(f"Digite o valor {i + 1}: "))
    vetor.append(valor)

quantidade_diferentes = contar_valores_diferentes(vetor)
print(f"Quantidade de valores diferentes no vetor: {quantidade_diferentes}")
print("---------------------------------")