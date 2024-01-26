def jogar():
    print("*********************")
    print("    JOGO DA FORCA    ")
    print("*********************")

    palavra_secreta = "banana"
    enforcou = False

    lista_acertada = ['_', '_', '_', '_', '_', '_']
    print(lista_acertada)

    while ('_' in lista_acertada):
        chute = input("Escolha uma letra: ")
        chute = chute.strip()

        contador = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                print("A letra {} foi encontrada na posição: {}".format(chute.upper(), contador))
                lista_acertada[contador] = chute.lower()
            contador += 1
        print(lista_acertada)

if __name__ == "__main__":
    jogar()