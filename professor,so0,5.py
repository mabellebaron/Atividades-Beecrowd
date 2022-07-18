valordiv = int(input())
mensal = int(input())
parc = 1
while valordiv > 0:
    print(f'pagamento: {parc}')
    print(f'antes = {valordiv}')
    valordiv -= mensal
    if valordiv < 0:
        print(f'depois = 0')
    else:
        print(f'depois = {valordiv}')
    print('-'*5)
    parc += 1
    