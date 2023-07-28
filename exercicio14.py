valor = float(input('Digite o valor do notebook: R$'))
compra_pix = valor - (valor * 10 / 100)
compra_credito = valor + (valor * 5 / 100)

print("Comprando no pix, o produto sairá por R${:.2f}".format(compra_pix))
print("Comprando no credito, o valor sairá por R${:.2f}".format(compra_credito))
