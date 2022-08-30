km = float(input('Qual a quantidade de km percorridos?'))
dias = int(input('Foram quantos dias de aluguel? '))
pago = (km * 0.15) + (dias * 60)
print('O preço a se pagar pelo aluguel de {} dias, e {} km, é de R${:.2f}!'.format(dias, km, pago))
