from tkinter import *

number_1 = input('Entre com seu primeiro numero: ')
number_2 = input('Entre com seu segundo numero: ')

Output
Entre com seu primeiro numero 'number_1': 5
Entre com seu segundo numero 'number_2': 7

number_1 = int(input('Entre com seu primeiro numero: '))
number_2 = int(input('Entre com seu segundo numero: '))

Output
Entre com seu primeiro numero 'number_1': 23
Entre com seu segundo numero 'number_2': 674

Output
Entre com seu primeiro numero 'number_1': 'soma'
number_1 = int(input('Entre com seu priemeiro numero: '))
ValueError: letra invalida for int() with base 10: 'soma'


number_1 = int(input('Entre com seu primeiro numero: '))

number_2 = int(input('Entre com seu segundo numero: '))

print(number_1 + number_2)

Output
Entre com seu primeiro numero 'number_1': 8
Entre com seu segundo numero 'number_2': 3

number_1 = int(input('Entre com seu primeiro numero: '))
number_2 = int(input('Entre com seu segundo numero: '))

print('{} + {} = '.format(number_1, number_2))
print(number_1 + number_2)

Output
Entre com seu primeiro numero 'number_1': 90
Entre com seu segundo numero 'number_2': 717
90 + 717 =
807

number_1 = int(input('Entre com seu primeiro numero: '))
number_2 = int(input('Entre com seu segundo numero: '))

print('{} + {} = '.format(number_1, number_2))
print(number_1 + number_2)

print('{} - {} = '.format(number_1, number_2))
print(number_1 - number_2)

print('{} * {} = '.format(number_1, number_2))
print(number_1 * number_2)

print('{} / {} = '.format(number_1, number_2))
print(number_1 / number_2)




operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

number_1 = int(input('Entre com seu primeriro numero: '))
number_2 = int(input('Entre com seu segundo numero: '))

print('{} + {} = '.format(number_1, number_2))
print(number_1 + number_2)

print('{} - {} = '.format(number_1, number_2))
print(number_1 - number_2)

print('{} * {} = '.format(number_1, number_2))
print(number_1 * number_2)

print('{} / {} = '.format(number_1, number_2))
print(number_1 / number_2)

operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

number_1 = int(input('Entre com seu primeiro numero: '))
number_2 = int(input('Entre com seu segundo numero: '))

if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

else:
    print('Você não digitou um operador válido, execute o programa novamente.')


Por favor, insira o primeiro number: 58
Por favor, insira o segundo number: 40
58 * 40 =
2320


def calculate():
    operation = input('''
Digite a operação matemática que deseja concluir:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

number_1 = int(input('Digite o primeiro número: '))
    number_2 = int(input('Digite o segundo número: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você não digitou um operador válido, por favor execute o programa novamente.')

calculate()

...
def again():

    # Take input from user
    calc_again = input('''
Deseja calcular novamente?
Digite Y para SIM ou N para NÃO.

''')

    if calc_again == 'Y':
        calculate()

    elif calc_again == 'N':
        print('depois voce ve.')

    else:
        again()

calculate()

...
def again():
    calc_again = input('''
Deseja calcular novamente?
Digite Y para SIM ou N para NÃO.
''')

    if calc_again.upper() == 'Y':
        calculate()

    elif calc_again.upper() == 'N':
        print('See you later.')

    else:
        again()

def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again?

Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()


def welcome():
    print('''
Welcome to Calculator
''')
...
welcome()
calculate()

...
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
** for power
% for modulo
''')
...