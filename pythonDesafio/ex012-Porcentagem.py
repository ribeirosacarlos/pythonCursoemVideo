produto = float(input('Digite o preço do produto: R$'))
porcentagem = (5 / 100) * produto
novoPreco = produto - porcentagem
print('O preço do produto com desconto é de R${} reais.'.format(novoPreco))


