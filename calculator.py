"""
#과제 1 사칙연산 계산기 프로그램을 만들어주세요.

사용자로부터 "숫자 연산자 숫자" 를 입력받아 결과값을 출력해주세요.
사용자가 c를 입력하면 다시 입력받아야하고 e를 입력하면 계산기가 종료되어야합니다.
e를 입력하기 전까지는 계산기가 끝나면 안됩니다.
숫자나 연산자를 잘못 입력하면 다시 입력받도록 해주세요.
"""

while True:
    number1 = input("첫번째 숫자:")
    if number1 == 'e':
        break
    elif number1 == 'c':
        continue
    while not number1.isdigit():
        number1 = input("다시 입력해주세요:")

    operator = input("연산자:")
    if operator == 'e':
        break
    elif operator == 'c':
        continue
    while operator not in ['+', '-', '/', '*']:
        operator = input("다시 입력해주세요:")

    number2 = input("두번째 숫자:")
    if number2 == 'e':
        break
    elif number2 == 'c':
        continue
    while not number2.isdigit():
        number2 = input("다시 입력해주세요:")

    if operator == '+':
        print(int(number1) + int(number2))

    if operator == '-':
        print(int(number1) - int(number2))

    if operator == '/':
        print(int(number1) / int(number2))

    if operator == '*':
        print(int(number1) * int(number2))
