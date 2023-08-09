valor = float (input('Valor do item'))
qtd = int (input('Quantidade'))

total = valor * qtd
valor_descontado = total * 0.10
total_fixo = total - valor_descontado

desconto_unidade = total_fixo * 0.1
total_unidade = total_fixo - desconto_unidade

# Exibir tudo
print ('Valor original:R$', valor * qtd)
print ('Valor pago:R$', total - valor_descontado)
