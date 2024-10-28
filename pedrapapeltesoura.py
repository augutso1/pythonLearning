import random

opcoes = ["pedra", "papel", "tesoura"]

pontos_usuario = 0
pontos_maquina = 0
empates = 0

while True:
    escolha_usuario = input("Escolha sua jogada ou envie 's' para sair: ").lower()

    if escolha_usuario == "s":
        break
    
    if escolha_usuario not in opcoes:
        print("Por favor selecione uma opção válida.")
        continue

    num_aleatorio = random.randint(0, 2)
    escolha_maquina = opcoes[num_aleatorio]


    print("O computador escolheu", escolha_maquina + ".")
    
    if escolha_maquina == escolha_usuario:
        empates += 1 
        print("Empate.")

    elif escolha_usuario == "pedra" and escolha_maquina == "tesoura":
        pontos_usuario += 1 
        print("Você venceu!")

    elif escolha_usuario == "papel" and escolha_maquina == "pedra":
        pontos_usuario += 1 
        print("Você venceu!")

    elif escolha_usuario == "tesoura" and escolha_maquina == "papel":
        pontos_usuario += 1 
        print("Você venceu!")

    else:
        pontos_maquina += 1 
        print("Você perdeu...")

print("Você fez", pontos_usuario, "pontos")
print("A máquina fez", pontos_maquina, "pontos")
print("Houveram", str(empates), "empates.")