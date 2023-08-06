#função setando os valores dos sabores
def calcValor (sabor, quant):
  precos = {
    'tr': [6, 10, 14],
    'pr': [7, 12, 17],
    'es': [8, 14, 20] 
  }

  #valor do pedido
  valorPedido = precos[sabor][quant-1]
  return valorPedido

#variavel que recebe os valores totais dos pedidos
valor_total = 0

#print do cardapio
print ('Bem-vindo a Sorveteria do Abraao Rocha de Paula')
print ('-----------------------------------------Cardapio------------------------------------------')
print ('| N DE BOLAS    |    Sabor Tradicional(tr) |    Sabor Premium(pr) |    Sabor Especial(es) |')
print ('|      1        |          R$6             |          R$7         |           R$8         |')
print ('|      2        |          R$10            |          R$12        |           R$14        |')
print ('|      3        |          R$14            |          R$17        |           R$20        |')
print ('-------------------------------------------------------------------------------------------')

#estrutura do pedido e catch de erros
while True:
  sabor = input('Selecione o sabor (tr/pr/es): ')
  if sabor not in ['tr', 'pr', 'es']:
    print('Sabor invalido')
    continue
  
  quant = int(input('Digite a quantidade de bolas de sorvete (1/2/3): '))
  if quant not in [1, 2, 3]:
    print('Quantidade de bolas de sorvete invalida')
    continue

  valor = calcValor(sabor, quant)

  if valor is not None:
    valor_total += valor
    print(f'Você pediu {quant} bolas de sorvete sabor {sabor} com o valor de R$ {valor}')

  opcao = input('Deseja continuar? (s/n): ')
  if opcao.lower() != 's':
    print(f'Valor total a ser pago: R$ {valor_total}')
    break
