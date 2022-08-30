largura = float(input('Digite a largura da sua parede: '))
altura = float(input('Digite a altura da sua parede: '))
m2 = largura * altura
litroTinta = m2 / 2
convertedInt = int(litroTinta)
print('É necessário {} de tinta para pintar essa parede.'.format(convertedInt))