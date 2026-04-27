# While - faz algo enquanto a condição for verdadeira
"""
teste = 0
while teste<=5:
    print(f"Teste é igual à {teste}")
    teste += 1
"""

# continue skipa tudo da repetição

"""

teste = 0
while teste<=10:
    teste += 1
    if teste == 3:
        continue
    else:
        print(f"Teste é igual à {teste}")
"""

# Usando o While pra validação
"""
def validacao(nota):
    while nota<0 or nota>10:
        print("A nota deve estar entre 0 e 10")
        nota = float(input("digite a nota novamente:"))
    return nota


notaA = float(input("Digite a 1° nota: "))
notaA = validacao(notaA)

notaB = float(input("Digite a 2° nota: "))
notaB = validacao(notaB)

media = (notaA+notaB)/2
print(f"A média das notas {notaA} e {notaB} é: {media}")
"""

# For é usado para repetir uma quantidade de vezes específicas
"""
teste = 0
for i in range(0,11,1):
    print(f"O Valor do teste é: {teste}")
    teste += 1
"""



