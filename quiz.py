estado=bool

jogando=input("Você quer jogar um QUIZ? ")

score=0

if jogando.lower() == 'sim':
    estado=True
else:
    estado=False
    quit()

if estado == True:
    print("Certo, vamos começar nosso quiz.")
    
    resposta=input("Qual a primeira letra do alfabeto? ")
    if resposta.lower() == 'a':
        print("Resposta correta!")
        score+=1
    else :
        print("Resposta incorreta...")
    
    resposta=input("Qual a segunda letra do alfabeto? ")
    if resposta.lower() == 'b':
        print("Resposta correta!")
        score+=1
    else :
        print("Resposta incorreta...")
        
    resposta=input("Qual a terceira letra do alfabeto? ")
    if resposta.lower() == 'c':
        print("Resposta correta!")
        score+=1
    else :
        print("Resposta incorreta...")
        
    resposta=input("Qual a quarta letra do alfabeto? ")
    if resposta.lower() == 'd':
        print("Resposta correta!")
        score+=1
    else :
        print("Resposta incorreta...")
print("Você acertou " + str(score) + " perguntas!")
print("Você completou " + str((score/4)*100) + "% do QUIZ")


