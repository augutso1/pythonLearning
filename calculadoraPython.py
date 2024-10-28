def obter_numero(mensagem):
    while True:
        try:
            numero = input(mensagem)
            numero = int(numero)
            return numero
        except ValueError:
            try:
                numero = float(numero)
                return numero
            except ValueError:
                print("Por favor, insira um número válido.")
# função para definir a tipagem do número escrito pelo usuário
operadores = {'*', '/', '+', '-', 'S', 's'}
# lista com os operadores
while True:
    operacao = input("Escolha qual operação deseja realizar ('*': MULTIPLICAÇÃO, '/': DIVISÃO, '+': ADIÇÃO, '-': SUBTRAÇÃO, 'S': Fechar programa): ").lower()

    if len(operacao) == 1 and operacao in operadores:
        # verifica se a operação é válida, se sim, continua o programa
        if operacao == '*':
            num = obter_numero("Escreva o número a ser multiplicado: ")
            multiplicador = obter_numero("Escreva o número multiplicador: ")
            resultado = num * multiplicador
            print("O resultado é:", resultado)

        elif operacao == '/':
            dividendo = obter_numero("Escreva o número dividendo: ")
            divisor = obter_numero("Escreva o número divisor: ")
            if divisor != 0:
                # verifica se o divisor é 0, pois divisão por 0 não existe
                resto = dividendo % divisor
                resultado = dividendo / divisor
                print("O resultado é:", resultado, ", com resto igual a:", resto)
            else:
                print("Erro: Divisão por zero não é permitida.")

        elif operacao == '+':
            num1 = obter_numero("Escreva o primeiro número da adição: ")
            num2 = obter_numero("Escreva o segundo número da adição: ")
            resultado = num1 + num2
            print("O resultado é:", resultado)

        elif operacao == '-':
            num1 = obter_numero("Escreva o primeiro número da subtração: ")
            num2 = obter_numero("Escreva o segundo número da subtração: ")
            resultado = num1 - num2
            print("O resultado é:", resultado)

        elif operacao == 's':
            print("Programa encerrado.")
            break
    else:
        print("Operação inválida. Por favor, escolha uma operação válida.")
