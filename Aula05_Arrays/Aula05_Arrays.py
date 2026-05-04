"""
# Uma string também seria um "Array"
texto = "FIAP Paulista"
print(texto[0])
print(texto[1])
print(texto[2])
print(texto[3])

print("---------------------------")

tamanho = len(texto)
for i in range(tamanho):
    print(f"Texto de [{i}] = {texto[i]}")
"""

"""
lista = ["A","B","C","D","E"]
print(lista)
print(len(lista))

# Append add novo item na última posição
lista.append("F")
print(lista)
print(len(lista))

for item in lista:
    print(item)
"""

"""
# Atividade 1:
# Dado um conjunto de nomes de quatro pessoas, escreva um algoritmo que imprima todas as possíveis duplas que podem ser formadas.
# Primeiro, crie um vetor e coloque quatro nomes nele.
# A seguir, exiba as possíveis duplas

nomes = ["Max","Bob","Ana","Ju"]
dupla_n=1

for i in range(len(nomes)):
    for j in range(i+1,len(nomes)):
        print(f"Dupla {dupla_n}: {nomes[i]} e {nomes[j]}")
        dupla_n+=1
"""

"""
# Matrizes

tabuleiro = [
    ["","",""],
    ["","",""],
    ["","",""]
]
tabuleiro [0][0] = "x"
tabuleiro [1][1] = "x"
tabuleiro [2][2] = "x"
print(f"{tabuleiro[0]} \n{tabuleiro[1]}\n{tabuleiro[2]}")
"""
