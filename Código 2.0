resposta = ''
resposta2 = ''
resposta3 = ''
resposta4 = ''
resultado = 0
numeroOP = 2

num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))
num = input('Informe a operação:' +
            ' "+", "-", "+", "*", "/": ')
if num == '+':
    resultado = num1 + num2
    print(f'O resultado da soma é {resultado}')
if num == '-':
    if num1 > num2:
        resultado = num1 - num2
        print(f'O resultado da subtração é {resultado}')
    if num2 > num1:
        resultado = num2 - num1
        print(f'O resultado da subtração é {resultado}')
if num == '*':
    resultado = num1 * num2
    print(f'O resultado da multiplicação é {resultado}')
if num == '/':
    if num1 > num2:
        resultado = num1 / num2
        print(f'O resultado da divisão é {resultado}')
    if num2 > num1:
        resultado = num2 / num1
        print(f'O resultado da divisão é {resultado}')
resposta = input('Deseja fazer uma nova operação? ')

if resposta == 'não':
    print(f'O resultado final da operação é {resultado}')
elif resposta == 'sim':
    while resposta2 != 'não':
        print(f'{numeroOP}ª operação')
        resposta4 = float(input('Informe o novo número: '))
        resposta3 = input('Deseja fazer qual operação:' +
                          ' "+", "-", "+", "*", "/": ')
        if resposta3 == '+':
            resultado = resultado + resposta4
            print(f'O resultado da nova soma é {resultado}')
        if resposta3 == '-':
            if resultado > resposta4:
                resultado = resultado - resposta4
                print(f'O resultado da nova subtração é {resultado}')
            if resposta4 > resultado:
                resultado = resposta4 - resultado
                print(f'O resultado da nova subtração é {resultado}')
        if resposta3 == '*':
            resultado = resultado * resposta4
            print(f'O resultado da nova multiplicação é {resultado}')
        if resposta3 == '/':
            if resultado > resposta4:
                resultado = resultado / resposta4
                print(f'O resultado da nova divisão é {resultado}')
            if resposta4 > resultado:
                resultado = resposta4 / resultado
                print(f'O resultado da divisão é {resultado}')

        numeroOP += 1
        resposta3 = input('Deseja fazer uma nova operação: ')
        if resposta3 == 'não':
            resposta2 = resposta3
            print(f'O resultado final é {resultado}')
        elif resposta3 == 'sim':
            print('Repetir operação!')
