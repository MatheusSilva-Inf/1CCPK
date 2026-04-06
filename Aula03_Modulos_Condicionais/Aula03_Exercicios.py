"""
# Desafio: Receba a idade e indique se o voto é opcional

idade = int(input("Digite sua Idade: "))

if (idade>= 70 or (idade >=16 and idade <18)):
    print("Seu voto é facultativo")
elif(idade<16):
    print("Não pode votar")
else:
    print("Voto Obrigatório")
"""
from typing import final

"""
# Exercício 1: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3

musicas = [0,1,2,3,4,5,6,7,8,9,10]

def tocar_musica(music):
    return music

input("Escolha a música que deseja ouvir dentro da playlist")
"""

"""
# Exercício 2: Faça um programa que leia um número, e informe se ele é par ou impar.

def par_impar(num):
    if (num%2 == 0):
        print("Número par")
    else:
        print("Número ímpar")
par_impar(int(input("Digite um número: ")))
"""

"""
# Exercício 3: Faça um programa que peça dois números e imprima o maior deles, e informe caso eles sejam iguais.

def maior_num(num_1,num_2):
    if num_1>num_2:
        print(f"O maior valor é {num_1}")
    elif num_2>num_1:
        print(f"O maior valor é {num_2}")
    else:
        print("Os valores são iguais")
print("Você deve digitar dois números e o maior será descrito")
maior_num(int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")))
"""

"""
# Exercício 4: Faça um programa para a leitura de quatro notas parciais de um aluno. O programa deve calcular a
# média alcançada pelo aluno e apresentar:
# ▪ A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# ▪ A mensagem "Em recuperação", se a média for entre cinco, incluindo o cinco, e sete;
# ▪ A mensagem "Reprovado", se a média for menor que cinco


def calcularmedia(nota):
    media = sum(nota)/len(nota)
    if media >=7:
        print("Aprovado")
    elif media<5:
        print("Reprovado")
    else:
        print("Em Recuperação")

notas = []
notas.extend([int(input("Digite a primeira nota: ")),int(input("Digite a segunda nota: ")),int(input("Digite a terceira nota: ")),int(input("Digite a quarta nota: "))])
calcularmedia(notas)
"""

"""
# Exercício 5: EXERCÍCIO 5
# Faça um programa que leia 2 valores inteiros (A e B).
# A seguir, o programa deve mostrar uma mensagem "São Múltiplos" ou "Não são Múltiplos", indicando se os valores lidos são múltiplos entre si.
# Dica:
# Como que eu sei que 2 números são ou não são múltiplos um do outro?
# Conjunto dos Múltiplos de 2 = {2, 4, 6, 8, 10, ...}
# Então se observa que os múltiplos de um número são divisíveis por esse número, então o resto dessa divisão será 0.

def multiplos(num_a,num_b):
    if (num_a%num_b == 0 or num_b%num_a==0):
        print(f"Os números: {num_a} e {num_b} são múltiplos.")
    else:
        print(f"os números {num_a} e {num_b} não são múltiplos")

print("Digite dois números para saber se são múltiplos")
multiplos(int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")))
"""
"""
# Exercício 6: Escreva um algoritmo que recebe dois números e um caractere (representando uma das operações
# matemáticas (+, -, *, /)
# ▪ O programa deve calcular o valor final de acordo com a operação selecionada.
# ▪ Ou seja, se a entrada for 5, 6 e *, então seu programa dever mostrar 30.

def calculadora_bas(num_a,num_b,operador):
    if operador == "+":
        print(f"a operação de {num_a} + {num_b} é igual à: {num_a+num_b}.")
    elif operador == "-":
        print(f"a operação de {num_a} - {num_b} é igual à: {num_a-num_b}.")
    elif operador == "*":
        print(f"a operação de {num_a} * {num_b} é igual à: {num_a*num_b}.")
    elif operador == "/":
        print(f"a operação de {num_a} / {num_b} é igual à: {num_a/num_b}.")
    else:
        print("Operador inválido, tente novamente")
        calculadora_bas(int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")),
                        input("Digite o operador: "))

print("Digite dois números e um operador dentre: + , -, *, /")
calculadora_bas(int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")), input("Digite o operador: "))
"""

"""
# Exercício 7: Faça um programa que receba o ano de nascimento da pessoa e retorne:
# ▪ Se o voto é obrigatório este ano;
# ▪ Se o voto é opcional este ano;
# ▪ Se o voto é proibido este ano.

def voto(ano):
    ano_atual = 2026
    idade_ano= 2026 - ano
    if (idade_ano >= 70 or (idade_ano >= 16 and idade_ano < 18)):
        print("Seu voto é opcional este ano")
    elif (idade_ano < 16):
        print("Seu voto é proibido este ano")
    else:
        print("Seu voto é obrigatório esse ano")

voto(int(input("Digite seu ano de nascimento: ")))

"""

"""
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# ▪ Salários até R$ 280,00 (incluindo): aumento de 20%.
# ▪ Salários entre R$ 280,00 e R$ 700,00: aumento de 15%.
# ▪ Salários entre R$ 700,00 e R$ 1500,00: aumento de 10%.
# ▪ Salários de R$ 1500,00 em diante: aumento de 5%.
# ▪ Após o aumento ser realizado, informe na tela:
# ▪ O salário antes do reajuste.
# ▪ O percentual de aumento aplicado.
# ▪ O valor do aumento.
# ▪ O novo salário, após o aumento

def salario(salario):
    if salario >1500:
        aumento = 0.05
    elif salario>700:
        aumento = 0.10
    elif salario >280:
        aumento = 0.15
    else:
        aumento = 0.20


    print(f"O Salário antes do reajuste é: {salario}")
    print(f"O percentual do aumento é {aumento*100:.0f}%")
    print(f"O valor do aumento é: {salario*aumento}")
    print(f"o novo salário é {salario+salario*aumento}")

salario(float(input("Digite seu salário: ")))
"""

"""
# Exercício 9: Faça um programa que recebe:
# ▪ o código do estado de origem da carga de um caminhão, supondo que é um número inteiro de 1 a 5
# ▪ o peso da carga do caminhão em toneladas
# ▪ o código da carga, supondo que é um número inteiro de 10 e 40
# ▪ Seu programa deve calcular:
# ▪ o peso da carga do caminhão convertido em quilos
# ▪ o preço da carga do caminhão
# ▪ valor do imposto que e cobrado com base no preço da carga e do estado de origem
# ▪ o valor total transportado pelo caminhão (carga + impostos)

def caminhao(codigo_estado,peso_carga_toneladas,codigo_carga):
    impostos = [35,25,15,5,0]
    peso_kg = peso_carga_toneladas*1000

    if codigo_carga in range(10,41):
        if codigo_carga<21:
            preco_carga = 100
            preco_total = 100*peso_kg
        elif codigo_carga<31:
            preco_carga=250
            preco_total=250*peso_kg
        else:
            preco_carga = 340
            preco_total = 340 * peso_kg
    else:
        print("O código da carga é inválido")
    if codigo_estado in range(1,6):
        codigo =codigo_estado
        match codigo:
            case 1:
                imposto = 35
                valor_imposto=preco_total*(imposto/100)
            case 2:
                imposto = 25
                valor_imposto = preco_total * (imposto / 100)
            case 3:
                imposto = 15
                valor_imposto = preco_total * (imposto / 100)
            case 4:
                imposto = 5
                valor_imposto = preco_total * (imposto / 100)
            case 5:
                imposto = 0
                valor_imposto = 0
            case _:
                print("Erro")
    else:
        print("O código do estado é inválido")

    valor_final = preco_total-valor_imposto
    print(f"O Peso total do caminhão em Quilogramas é: {peso_kg}")
    print(f"O preço da carga sem imposto é: {preco_total}")
    print(f"O percentual de imposto é: {imposto}")
    print(f"O valor final que será recebido é: {valor_final}")


caminhao(int(input("Digite o código do estado: ")),int(input("Digite o peso em o tonelada: ")),int(input("Digite o código de carga: ")))
"""

"""
# Exercício 10: Faça um programa que leia 3 valores que representam os lados de um triângulo A, B e C e ordene-os
# em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o
# tipo de triângulo que estes três lados formam, com base nos seguintes casos:
# ▪ Se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO;
# ▪ Se A² = B² + C² , apresente a mensagem: TRIANGULO RETANGULO;
# ▪ Se A² > B² + C² , apresente a mensagem: TRIANGULO OBTUSANGULO;
# ▪ Se A² < B² + C² , apresente a mensagem: TRIANGULO ACUTANGULO;
# ▪ Se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO;
# ▪ Se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES;

def triangulo(lados):
    lados.sort(reverse=True)
    print(lados)
    if lados[0]>=lados[1]+lados[2]:
        print("Não forma triângulo")
    elif lados[0]**2 == lados[1]**2+lados[2]**2:
        print("Triângulo Retângulo")
    elif lados[0]**2 > lados[1]**2+lados[2]**2:
        print("Triângulo Obtusângulo")
    elif lados[0] ** 2 < lados[1] ** 2 + lados[2] ** 2:
        print("Triângulo Acutângulo")
    elif lados[0] == lados[1] and lados[0] ==lados[2]:
        print("Triângulo Equilátero")
    elif lados[0] == lados[1] or lados[0] == lados[2] or lados[1]==lados[2]:
        print("Triângulo Isóceles")

lados = []
lados.extend([float(input("Digite o primeiro lado: ")),float(input("Digite o segundo lado: ")),float(input("Digite o terceiro lado: "))])
triangulo(lados)
"""