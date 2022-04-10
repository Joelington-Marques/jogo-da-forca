def jogar():
    print('****************************************')
    print('****** Bem-vindo ao jogo da forca ******')
    print('****************************************')

    palavra_secreta = "banana"
    letras_acertas =["_","_","_","_","_","_"]


    enforcou = False
    acertou =

    print(letras_acertadas)

    while (not acertou and not enforcou):

        chute = input("Qual letra?")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertas[index] = letra
            index = index +1

        print(letras_acertadas)

    print("Fim do jogo")

if(__name__ == '__main__'):
    jogar()