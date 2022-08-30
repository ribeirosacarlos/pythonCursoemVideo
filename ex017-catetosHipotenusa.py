import math
catetoOposto = float(input('Digite o cateto Oposto de um Triangulo Retângulo: '))
catetoAdjacente = float(input('Digite o cateto Adjacente de um Triangulo Retângulo: '))

hipotenusa = math.sqrt((catetoOposto ** 2) + (catetoAdjacente ** 2))

#opção certa do math 'math.hypot()'
#hipotenusa = math.hypot(catetoOposto, catetoAdjacente)

print('O comprimento da hipotenusa do Cateto Oposto {}, e do Cateto Adjacente {} é {:.2f}'.format(catetoOposto, catetoAdjacente, hipotenusa))


'''
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
'''

# a² = b² + c²
# a² = (4²) + (3²)
# a² = 16 + 9
# a² = 25
# a = raizQuadrada(25)
# a = 5