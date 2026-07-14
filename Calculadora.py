print('\n      CALCULADORA')
print('----------------------')

while True:
  
    while True:
        n1 = input('\nSelecione o primeiro numero: ')
        try: 
            n1certo = float(n1)
            break
        except:
            print('Digita apenas numero por favor;')


    while True:
        n2 = input('\nSelecione o segundo numero: ')
        try: 
            n2certo = float(n2)
            break
        except:
            print('Digita apenas numero por favor;')

    print('\n----------------------\n1 -> Adição')
    print('2 -> Subtração')
    print('3 -> Multiplicação')
    print('4 -> Divisão\n')

    while True:
        operador = input('Selecione um Operador: ')
        try:
            selecao = int(operador)
            break
        except:
            print('Selecione uma das opções.\n')

    print('')

    if selecao == 1:
        print(f'A soma de {n1} e {n2} é igual a {n1certo + n2certo}')

    elif selecao == 2:
        print(f'A subtração de {n1} e {n2} é igual a {n1certo - n2certo}')

    elif selecao == 3:
        print(f'A multiplicação de {n1} e {n2} é igual a {n1certo * n2certo}')

    elif selecao == 4:
        print(f'A divisão de {n1} e {n2} é igual a {n1certo / n2certo}')



                    #Vi os metodos lower e startswith no curso
    sair = input('\nDeseja Sair? ').lower().startswith('s')
    if sair:
        break


