def calculator():
    number1 = int(input('n1: '))
    operator = str(input('Operador: '))
    number2 = int(input('n2:' ))
    if operator == '+':
        resultado = (number1 + number2)
    if operator == '-':
        resultado = (number1 - number2)
    if operator == '/':
        resultado = (number1 / number2)
    if operator == '*':
        resultado = (number1 * number2)
    print(resultado)
        
