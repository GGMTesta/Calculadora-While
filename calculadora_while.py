
while True:
    print ('iniciando')
    numero1 = input ('digite um numero: ')
    numero2 = input ('digite outro numero: ')
    operador = input ('digite um operador (+,-,/,*): ')

    numeros_validos = None

    try:
        num1_float = float(numero1)
        num2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print ('Um ou ambos os números digitados são inválidos.')
        continue    

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print ('operador invalido.')
        continue    

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue    
    
    print('Realizando sua conta, confira o resultado:')

    if operador == '+':
        print (f'{num1_float} + {num2_float} =', num1_float + num2_float)
    elif operador == '-':
        print (f'{num1_float} - {num2_float} =', num1_float - num2_float)
    elif operador == '/':
        print (f'{num1_float} / {num2_float} =', num1_float / num2_float)
    elif operador == '*':
        print (f'{num1_float} * {num2_float} =', num1_float * num2_float)             

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break

