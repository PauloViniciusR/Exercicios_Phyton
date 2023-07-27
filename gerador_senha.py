"""
Security = chave
5ecur1ty = senha
"""

chave = input("Digite a base da sua senha: ")

senha = ""
for letra in chave:
    if letra in "Aa": senha = senha + "10"
    elif letra in "Bb": senha = senha + "@"
    elif letra in "Cc": senha = senha + "5"
    elif letra in "Dd": senha = senha + "3"
    elif letra in "Ee": senha = senha + "4"
    elif letra in "Ff": senha =  senha + "15"
    elif letra in "Pp": senha = senha + "#"
    elif letra in "Ss": senha = senha + "%"
    elif letra in "Mm": senha = senha + "$"
    else: senha = senha + letra
print(senha)

