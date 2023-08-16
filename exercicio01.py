#Dada a lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52] faça um programa que:
# a) imprima o maior elemento
# b) imprima o menor elemento
# c) imprima os números pares
# d) imprima o número de ocorrências do primeiro elemento da lista
# e) imprima a média dos elementos
# f) imprima a soma dos elementos de valor negativo

lista =[12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
# Exercicio A
maior_elemento = lista[0] 

for elemento in lista:
    if elemento > maior_elemento:
        maior_elemento = elemento

print("O maior elemento na lista é:", maior_elemento)

#  Exercicio B
menor_elemento = lista[0]

for elemento in lista:
    if elemento < menor_elemento:
        menor_elemento = elemento

print("O menor elemento da lista é: ", menor_elemento)

print("-----------------------------------------------")

# Exercicio C
for numero in lista:
    if numero % 2 == 0:
        print(numero)

print("------------------------------------------------")
# Exercico D
primeiro_elemento = lista[0]
ocorrencias_primeiro = lista.count(primeiro_elemento)
print("Número de ocorrências do primeiro elemento:", ocorrencias_primeiro)
print("------------------------------------------------")
# Exercicio E
media = sum(lista) / len(lista)
print("Média dos elementos:", media)

print("-------------------------------------------------")
# Exercicio F
negativos = [num for num in lista if num < 0]
soma_negativos = sum(negativos)
print("Soma dos elementos de valor negativo:", soma_negativos)


         
     

