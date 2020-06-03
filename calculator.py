"""
#과제 1 사칙연산 계산기 프로그램을 만들어주세요.

사용자로부터 "숫자 연산자 숫자" 를 입력받아 결과값을 출력해주세요.
사용자가 c를 입력하면 다시 입력받아야하고 e를 입력하면 계산기가 종료되어야합니다.
e를 입력하기 전까지는 계산기가 끝나면 안됩니다.
숫자나 연산자를 잘못 입력하면 다시 입력받도록 해주세요.
"""


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


while True:
    print("종료하려면 e, 재시작을 하시려면 c를 입력해주세요.")
    num = input('계산식을 입력해주세요:')
    if num == 'e':
        break
    elif num == 'c':
        continue

    if '+' in num:
        a, b = num.split('+')
        operator = '+'

    elif '-' in num:
        a, b = num.split('-')
        operator = '-'

    elif '*' in num:
        a, b = num.split('*')
        operator = '*'

    elif '/' in num:
        a, b = num.split('/')
        operator = '/'

    else:
        print('잘못된 입력입니다. 올바른 연산자를 입력해주세요.')
        continue

    if not a.isdigit() or not b.isdigit():
        print("잘못된 입력입니다. 숫자를 입력해주세요.")
        continue

    if operator == '+':
        with open("calculator result.txt", 'a') as file:
            file.write("결과값은 %d입니다.\n" % add(int(a), int(b)))
            print("결과값은 %d입니다." % add(int(a), int(b)))

    elif operator == '-':
        with open("calculator result.txt", 'a') as file:
            file.write("결과값은 %d입니다.\n" % sub(int(a), int(b)))
            print("결과값은 %d입니다." % sub(int(a), int(b)))

    elif operator == '*':
        with open("calculator result.txt", 'a') as file:
            file.write("결과값은 %d입니다.\n" % mul(int(a), int(b)))
            print("결과값은 %d입니다." % mul(int(a), int(b)))

    elif operator == '/':
        with open("calculator result.txt", 'a') as file:
            file.write("결과값은 %d입니다.\n" % div(int(a), int(b)))
            print("결과값은 %d입니다." % div(int(a), int(b)))

