valor = float(input( 'Valor mercadoria: '))
qtd = int(input('Quantidade: '))

total = valor*qtd
desconto = total * (10 + qtd) / 100
final = total - desconto

print (f'{total:.2f}')
print(f'{final:.2f}')