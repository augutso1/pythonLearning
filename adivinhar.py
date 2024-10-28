import random

limite=input("Escreva um número: ")

if limite.lstrip('-').isdigit():
    limite=int(limite)
    if limite<=0:
        print("Por favor escreva um número maior que zero.")
        quit()
    else:
        print("Escreva um número for favor.")
        quit()

num_aleatorio=random.randint(0, limite)

tentativas=0

while True:
    tentativas+=1
    tentativa=input("Tente adivinhar: ")
    if tentativa.isdigit():
        tentativa=int(tentativa)
    else:
        print("Por favor escreva um número.")
        quit()
        continue
        
    if tentativa == num_aleatorio:
        print("Parabéns você acertou!")
        break
    else:
        if tentativa > num_aleatorio:
            print("O número é menor que", tentativa)
        elif tentativa < num_aleatorio:
            print("O número é maior que", tentativa)
print("Você levou", tentativas, "tentativas para acertar")