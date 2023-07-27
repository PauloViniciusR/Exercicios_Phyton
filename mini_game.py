palpite = ""
numero = 2

while True:
    print("Insira um numero: ")
    palpite = int(input())

    if palpite == numero:
        print("Parabéns, voce acertou")
        break
    else:
        print("Você errou")
