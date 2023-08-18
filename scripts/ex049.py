# Calcula o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista (dinheiro ou cheque): 10% de desconto;
# À vista no cartão: 5% de desconto;
# Em até 2 vezes no cartão: preço normal;
# 3x ou mais no cartão: 20% de juros.

print('--- Pagamento ---')
precoNormal = float(input('Qual o valor do produto? '))
if precoNormal > 0:
    print('Métodos de pagamento:\n'
          '[1] à vista no dinheiro ou cheque (desconto de 10%)\n'
          '[2] à vista no cartão (desconto de 5%)\n'
          '[3] em até 2x no cartão\n'
          '[4] em até 10x no cartão (com juros de 20%)'
          )
    metodoPagamento = int(input(f'Qual o método de pagamento? '))
    if 1 <= metodoPagamento <= 4:
        if metodoPagamento == 1:
            valorFinal = precoNormal - (precoNormal * 0.10)
            print(
                f"O valor do produto é R${precoNormal:.2f}, à vista no dinheiro ou cheque têm desconto de 10% fica por R${valorFinal:.2f}")
        elif metodoPagamento == 2:
            valorFinal = precoNormal - (precoNormal * 0.05)
            print(
                f"O valor do produto é R${precoNormal:.2f}, à vista no cartão têm desconto de 5% e fica por R${valorFinal:.2f}")
        elif metodoPagamento == 3:
            valorParcelas = precoNormal / 2
            print(
                f"O valor do produto é R${precoNormal:.2f}, "
                f"você escolheu dividir em 2 parcelas de R${valorParcelas:.2f} sem juros no cartão. ")
        else:
            parcelas = int(input('Você pode parcelar de 3 à 10 vezes no cartão. Em quantas vezes você quer parcelar? '))
            if 3 <= parcelas <= 10:
                valorFinal = precoNormal + (precoNormal * 0.20)
                valorParcelas = valorFinal / parcelas
                print(
                    f"O valor do produto é R${precoNormal:.2f}, "
                    f"você escolheu dividir em {parcelas} parcelas, com juros de 20%, o valor das parcelas ficará por R${valorParcelas:.2f}. "
                    f"Ao todo, ficará por R${valorFinal:.2f}")
            else:
                print('Valor Inválido! Escolha o número de parcelas entre 3 e 10.')
    else:
        print('Método de Pagamento Inválido!')
else:
    print('Valor do Produto Inválido!')