#função que calcula o peso do cachorro e o valor base, também trata os erros de digitação do usuário
def cachorro_peso():
  while True:
    try:
      peso = float(input('Digite o peso do cachorro: '))
      if peso < 3:
         return 40
      elif 3 <= peso < 10:
        return 50
      elif 10 <= peso < 30:
        return 60
      elif 30 <= peso < 50:
        return 70
      else:
        print('Não aceitamos cachorros tão grandes.')
        print('Tente novamente.')
    except ValueError:
      print('Você digitou um valor não numérico.')
      print('Tente novamente.')

#função que calcula o multiplacador do valor base levando em consideração o tipo de pelo
def cachorro_pelo():
    while True:
        pelo = input('Digite o tipo de pelo do cachorro \n c - Pelo Curto \n m - Pelo Médio \n l - Pelo Longo \n >> ')
        if pelo in ['c', 'm', 'l']:
            return {'c': 1, 'm': 1.5, 'l': 2}[pelo]
        else:
            print("Opção inválida, por favor tente novamente.")

#função que recebe e calcula os extras desejados pelo usuário
def cachorro_extra():
    extras = 0
    while True:
        print('Deseja algum serviço adicional? \n 1 - Corte de unhas (10 reais) \n 2 - Limpeza de dentes (12 reais) \n 3 - Limpeza de orelhas (15 reais) \n 0 - Não desejo adicionais')
        
        try:
            adicional = int(input('Digite o número do serviço adicional desejado: '))
            if adicional == 0:
                return extras
            elif adicional in [1, 2, 3]:
                valor_extra = {1: 10, 2: 12, 3: 15}[adicional]
                extras += valor_extra
            else:
                print('Opção inválida, por favor tente novamente.')
        except ValueError:
            print('Por favor, digite um valor numérico.')

#função principal do código, chamando as funções acima e calculando o total do pedido
def main():
    print('Bem vindo ao Pet-Shop do Abraao Rocha de Paula')
    base = cachorro_peso()
    multiplicador = cachorro_pelo()
    extra = cachorro_extra()
    
    total = base * multiplicador + extra
        
    print(f'O valor total do seu pedido é R${total:.2f}')


#chamado da função principal
main()