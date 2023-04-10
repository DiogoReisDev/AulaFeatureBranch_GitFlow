def escolher_produtos():
    produtos = ['Hamburguer tradicional', 'Hamburguer vegano']
    print(produtos)
    select = input('Hamburguer tradicional digite 0: \nHamburguer Vegano digite 1: ')
    if select == 0:
        print('Você escolheu o Hamburguer tradicional!')
    elif select == 1:
        print('Você escolheu o Hamburguer Vegano!')
    else:
        print('Favor selecionar as opções disponíveis...')
escolher_produtos()