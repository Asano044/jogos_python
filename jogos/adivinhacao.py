import random as rd

def jogar():
    print("********************* \nJOGO DE ADIVINHAÇÃO \n*********************")

    numero_escolhido = rd.randrange(1, 101)

    pontos = 1000

    nivel = int(input("Escolha entre os níveis: (1) fácil (2) médio (3) difícil: "))
    if nivel == 1:
        tentativas = 15
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        resposta = int(input("Informe um número: "))

        if resposta < 1 or resposta > 100:
            print("Você deve digitar um número entre 1 e 100.")
            continue

        print("Você digitou o número ", resposta)
        if resposta == numero_escolhido:
            print("Você acertou!!")
            break
        else:
            if resposta > numero_escolhido:
                print("Sua resposta é maior que o número escolhido.")
            else:
                print("Sua resposta é menor que o número escolhido.")
            pontos = pontos - abs(numero_escolhido - resposta)

    print("Número secreto: " + str(numero_escolhido))
    print("Você concluiu o jogo com {} pontos.".format(pontos))
    print("Fim de jogo!")

if __name__ == "__main__":
    jogar()