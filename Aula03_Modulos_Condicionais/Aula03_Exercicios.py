idade = int(input("Digite sua Idade: "))

if ((idade>= 16 &  idade <18) | idade>= 70):
    print("Seu voto é facultativo")
elif(idade<16):
    print("Não pode votar")
else:
    print("Voto Obrigatório")