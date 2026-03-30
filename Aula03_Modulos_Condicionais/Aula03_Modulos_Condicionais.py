import math
import random
'''
# Raiz Quadrada importada do Math
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print(f"Raiz do número digitado: {raiz:.2f}")
'''

'''
# Funções do math relacionadas à graus
graus = int(input("Digite um ângulo: "))
radiano = graus/180*math.pi
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

 print(f"Seno: {seno:.2f}, Cosseno: {cosseno:.2f}, Tangente: {tangente:.2f}")
'''

'''
# Funções de randomização
num_random = random.Random()
print(num_random)

num_random_int = random.randint(1,100)
print(num_random_int)

num_random_range = random.randrange(1,100)
print(num_random_range)
'''

'''
# Funções Próprias, indentação importa

def calculo_angulo(angulo):
    radiano = angulo / 180 * math.pi
    seno = math.sin(radiano)
    cosseno = math.cos(radiano)
    tangente = math.tan(radiano)
    print(f"Seno: {seno:.2f}, Cosseno: {cosseno:.2f}, Tangente: {tangente:.2f}")
    
calculo_angulo(int(input("Digite um ângulo: ")))
'''

# Condicionais
'''
nota = float(input("Digite sua nota: "))
if nota>=6:
    print("Você passou")
else:
    print("Você Falhou")
print("Fim")
'''

'''
nota = float(input("Digite sua nota: "))
if nota>=9:
    print("Extraordinário")
elif nota >=7:
        print("Muito bom")
elif nota >=5:
        print("Medíocre")
elif nota >=3:
        print("Ruim")
else:
    print("Horrível")
print("Fim")
'''

'''
nota = float(input("Digite sua nota: "))
if nota<4:
    print("reprovado")
else:
    if nota <6:
        print("Recuperação")
    else:
        print("Aprovado")
print("Fim")
'''

# match case
'''
escolha_usuario = 0

match escolha_usuario:
    case 0:
        status = "Sair do Programa"
    case 1:
        status = "Entrar no programa"
    case _:
        status = "Erro"
print(status)
'''
