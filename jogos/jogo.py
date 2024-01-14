import forca
import adivinhacao

print("*********************")
print("   ESCOLHA UM JOGO   ")
print("*********************")

print("Qual jogo você deseja jogar? ")
resposta = int(input("(1)Forca (2)Adivinhação"))

if resposta == 1:
    print("Você escolheu o jogo da forca")
    forca.jogar()
elif resposta == 2:
    print("Você escolheu o jogo da adivinhação")
    adivinhacao.jogar()
else:
    print("Esta opção não está definida")
