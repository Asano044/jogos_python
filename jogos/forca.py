def jogar():
    print("*********************")
    print("    JOGO DA FORCA    ")
    print("*********************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        chute = input("Escolha uma letra: ")
        chute = chute.strip()

        contador = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                print("A letra {} foi encontrada na posição: {}".format(chute.upper(), contador))
            contador += 1
        print("jogando...")

if __name__ == "__main__":
    jogar()