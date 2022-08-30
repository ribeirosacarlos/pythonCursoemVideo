medida = float(input('Digite um valor em metros: '))
cm = medida * 100
mm = medida * 1000

print('{} metros, é igual a {:.0f}cm.\n{} metros, é igual a {:.0f}mm.'.format(medida, cm, medida, mm))
