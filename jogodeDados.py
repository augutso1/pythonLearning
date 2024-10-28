# usuário precisa rolar o dado
# perguntar se quer rolar mais 1x
# caso o usuário parar, SE ela não for = 1, armazenar sua pontuação em uma variável individual
# pontuação máxima de 20 pontos, verificar se a pontuação do usuário é igual a 20, caso seja, parar o programa e mostrar mensagem de vencedor

import random #módulo para conseguir números aleatórios

def rolar_dado ():
    rolar = random.randint(1, 6)
    #gerando número aleatório dentro do limite de um dado com 6 lados

    return rolar
    # retorna valor gerado aleatoriamente
# função para gerar número aleatório do dado
print(
    "Jogo de Dados:\n"
    "1: Você pode rolar o dado quantas vezes quiser;\n"
    "2: Caso você tire o número 1, sua pontuação para a rodada será 0;\n"
    "3: O primeiro jogador a fazer 20 pontos, vence a partida.\n"
    )
# regras do jogo
while True: #loop while para definir a quantidade de jogadores
    jogadores = input("Quantos jogadores irão participar? (2-4): ")

    if jogadores.isdigit(): # verifica se o input é um número ou não
        jogadores = int(jogadores) # como o input retorna tipo string, é preciso tranformá-lo em int

        if 2 <= jogadores <= 4: #verifica se o número de jogadores está dentro do limite e então para o laço e o programa continua
            break

        else:
            print("Por favor informe um valor entre 2 e 4")

    else:
        print("Número de jogadores inválido.")

pontuaçãoMax = 20

pontuaçãoJogadores = [0 for _ in range(jogadores)] # laço for que adiciona 0 para todos os jogadores presentes na partida
# range(jogadores): a função range gera números de 0 até jogadores - 1 (objeto iterável)
# o '0' é o elemento que será adicionado na lista
# o 'for _ in' inicia o laço ignorando o valor de index, percorrendo o range(jogadores) e substituindo os números por 0
while max(pontuaçãoJogadores) < pontuaçãoMax:
    # loop que roda enquanto nenhum jogador chegar na pontuação máxima
    for jogadores_i in range(jogadores): # laço de repetição que roda para cada jogador presente na partida
        print(f'\nRodada do jogador {jogadores_i + 1}:')
        print(f'Sua pontuação total é: {pontuaçãoJogadores[jogadores_i]}\n')
        pontuaçãoAtual = 0
        while True: # laço que repete as rodadas até que o jogador pare ou role 1 no dado
            rodada = input("Você gostaria de rolar ('r') o dado ou passar ('p') a vez? : ").lower()
            if rodada == 'r':
                valor = rolar_dado()
                if valor == 1:
                    print("Você rolou 1! rodada perdida...")
                    pontuaçãoAtual = 0;
                    break
                else:
                    pontuaçãoAtual += valor
                    print("Você rolou", valor)
                    print("Sua pontuação da rodada atual é:", pontuaçãoAtual)
                    continue

            elif rodada == 'p':
                break

        pontuaçãoJogadores[jogadores_i] += pontuaçãoAtual # soma da pontuação total do jogador em todas as rodadas
        print("Sua pontuação total é:", pontuaçãoJogadores[jogadores_i])

pontuaçãoMax = max(pontuaçãoJogadores) # inicia uma variável que recebe a pontuação máxima dentre os jogadores
vencedor_idx = pontuaçãoJogadores.index(pontuaçãoMax) # busca/encontra qual o índice do jogador com a maior pontuação
print("O jogador:", vencedor_idx + 1, "venceu a partida!")