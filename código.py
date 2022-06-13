
resposta = ''
resultado = 0
resultadoFinal = 0
while (resposta != 'não'):
    resposta = input('Deseja fazer uma operação: ')
    if resposta =='não':
        print('Saiu da aplicação')
    elif resposta == 'sim':
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

    else:
        print('Informações incorretas!')
