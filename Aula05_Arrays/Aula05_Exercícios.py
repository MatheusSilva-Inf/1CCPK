import random

"""
# Exercício 1:
# Escreva um algoritmo que recebe um número inteiro n > 0, cria um vetor de números reais com n
# posições e preenche o vetor com n números aleatórios reais.
# Depois de preenchido o vetor, imprima na tela todos os números gerados

qntd = int(input("Digite a quantidade de números à serem gerados (o número deve ser positivo): "))
while qntd<=1:
    qntd = int(input("Digite a quantidade de números à serem gerados (o número deve ser positivo): "))
vetor = []
for i in range(qntd):
    vetor.append(random.randint(1,100))
print(vetor)
"""

"""
# Exercício 2: 
# Considere uma turma de n alunos onde desejamos calcular a média das notas da prova semestral e
# saber quantas notas estão iguais, acima e abaixo dessa média.
# Escreva um algoritmo que lê um inteiro n representando a quantidade de alunos e cada uma das n
# notas e mostra a média da turma, quantas notas são iguais, acima e abaixo da média da turma.

alunos = int(input("Digite a quantidade de alunos: "))
notas = []

for i in range(alunos):
    # Se quiser ser aleatório
    # notas.append((random.randint(0,10)))
    # Se quiser ser manual
    notas.append(float(input(f"Digite a nota do Aluno {i+1}: ")))

media = sum(notas)/alunos
iguais = 0
acima = 0
abaixo = 0

for nota in notas:
    if nota == media:
        iguais+=1
    elif nota >media:
        acima+=1
    else:
        abaixo+=1
print(f"A Média da sala foi {media} \n {iguais} notas foram iguais à média\n {acima} notas foram acima da média \n{abaixo} notas foram abaixo da média")
"""

"""
# exercício 3:
# Faça um programa que tenha 2 vetores. Um vetor para os meses e outros para a quantidade de dias para cada mês.
# Seu programa deve exibir mensagens da seguinte forma:
# O Mês de Jan tem 31 dias ao todo.
# O mês de Fev tem 28 dias ao todo.
# O mês de Mar tem 31 dias ao todo.
# O mês de Dez tem 31 dias ao todo

mes_dia = [
    ["Janeiro",31],["Fevereiro",28],["Março",31],["Abril",30],["Maio",31],["Junho",30],
    ["Julho",31],["Agosto",31],["Setembro",30],["Outubro",31],["Novembro",30],["Dezembro",31]
]
for i in range (len(mes_dia)):
    print(f"O Mês de {mes_dia[i][0]} tem {mes_dia[i][1]} dias ao todo")
"""

"""
# Exercício 4:
# Escreva um algoritmo que lê um número inteiro n, cria um vetor de inteiros de tamanho n, faz a leitura
# de um conjunto de n números inteiros armazenando-os no vetor e depois calcula a somatória dos
# números contidos no vetor.
# ▪ Dica: note que a somatória deverá ser feita após o vetor estar preenchido.

qntd = int(input("Digite a quantidade de números à serem gerados (o número deve ser positivo): "))
while qntd<=1:
    qntd = int(input("Digite a quantidade de números à serem gerados (o número deve ser positivo): "))
vetor = []
for i in range(qntd):
    vetor.append(random.randint(1,100))
print(f"O vetor Gerado é: {vetor}")
print(f"A somatória dos números contidos no vetor acima é: {sum(vetor)}")
"""

"""
# Exercício 5
# ▪ Escreva um algoritmo que recebe uma lista de nomes e imprime os nomes na ordem inversa a da leitura.
# ▪ A lista termina quando o usuário aperta o Enter sem que nenhum nome tenha sido digitado.

nome = input("Digite um nome: ")
invertida = ""
lista = []
lista_inv = []

while nome!= "":
    invertida = ""
    lista.append(nome)
    for i in range(len(nome)-1,-1,-1):
        invertida += nome[i]
    lista_inv.append(invertida)
    nome = input("Continue digitando para aumentar a lista ou digite nada para parar: ")
print(f"A lista de nomes normais é: \n {lista}")
print(f"A lista de nomes invertidas é: \n {lista_inv}")
"""