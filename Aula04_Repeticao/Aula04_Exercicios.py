"""
Exercício 1:
- Faça um programa que exiba a mensagem “Olá, Mundo”.
- Essa mensagem deverá ser exibida repetidamente.
- Ao final de toda iteração da repetição, você deve perguntar ao usuário se ele deseja exibir a mensagem
novamente.
- Se sim, exiba novamente. Senão, saia do loop e exiba a mensagem “Fim”.
"""

"""

decisao: str = "sim"
while True:
    if decisao == "sim":
        print("Olá Mundo")
    elif decisao == "não":
        print("Fim")
        break
    else:
        print("O texto não foi identificado")
    decisao = input("Você deseja repetir a mensagem? Responda com sim ou não  ->  ")
"""


"""
Exercício 2: 
Contagem de 0 a 100 pulando de 10 em 10
"""
"""
contagem = 0

for i in range(0,11,1):
    print(contagem)
    contagem+=10
"""

"""
Exercício 3: 
Faça um programa que receba um número n e exiba a tabuada deste número do 0 ao 25.
"""

"""
numero = int(input("Digite um número para ver sua Tabuada: "))
contador = 0
for i in range (1,26,1):

    if i%numero ==0:
        contador+=1
        print(f"{numero}*{contador} = {i}")
"""

"""
Exercício 4: 
Faça um programa que receba 5 valores digitados pelo usuário e, ao final, informe qual é a soma deles.
"""

"""
soma = 0

for i in range (1,6,1):
    soma += int(input("Digite um valor para ser somado: "))
print(f"A soma é: {soma}")
"""

"""
Exercício 5: 
Faça um programa que receba 5 valores digitados pelo usuário e, ao final, informe qual é o maior deles.
"""
"""
maior = int(input("Digite um valor e no final será mostrado o maior digitado: "))
for i in range (1,6,1):
    novoValor = int(input("Digite um outro valor e no final será mostrado o maior digitado: "))
    if novoValor>maior:
        maior = novoValor
print(f"O maior valor escrito foi {maior}")
"""

"""
Exercício 6: 
Faça um programa capaz de exibir todos os valores pares entre 2 e um valor fornecido pelo usuário.
"""

"""
tamanho = int(input("Digite um valor para saber todos os números pares até ele: "))

for i in range(1,tamanho+1,1):
    if i%2==0:
        print(f"{i} é par")
"""

"""
Exercício 7: 
Escreva um programa que dado um inteiro n positivo calcula e imprime a soma de todos os números inteiros entre 1 e n.
Valide a entrada do usuário, só aceite números positivos!!
Dica: use while para a validação e for para a soma.
Por exemplo, se n = 10 então deverá ser calculado: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
E a impressão final seria: ▪ A soma de 1 até 10 é: 55.
"""

"""
n = int(input("Digite um número positivo para saber todas as somas entre 1 e ele: "))
soma = 0
while n<0:
    print("O número deve ser positivo")
    n = float(input("digite o número novamente:"))

for i in range (0,n+1,1):
    soma+=i

print(f"A soma de 1 até {n} é: {soma}")
"""

"""
Exercício 8: 
Escreva um algoritmo que recebe um inteiro positivo n e imprime todos os divisores positivos de n. Utilize o laço for.
▪ Exemplo: Suponha que n = 28, nessa situação devemos imprimir os números
1, 2, 4, 7, 14 e 28, que são todos os divisores do 28.
Dica: para o número ser divisor de n, a divisão precisa ter resto nulo.
"""

"""
n = int(input("Digite um número positivo para saber todos os divisores positivos dele: "))
while n<0:
    print("O número deve ser positivo")
    n = float(input("digite o número novamente:"))

for i in range(1,n+1,1):
    if n%i==0:
        print(f"{i} é divisor de {n}")
"""

"""
Exercício 9: 
Determine e mostre todos os números primos no intervalo de 2 a 2000.
"""

"""
for i in range(3,2001,1):
    primo = True
    for j in range(2,i,1):
        if i%j == 0:
            primo = False
            break
    if primo:
        print(f"{i} é um número primo")
"""