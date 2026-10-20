def calculator(num1, num2: int):
    try:
        answer = num1 / num2
        print(answer)
    except: print('cannot divide by 0')
num1 = 100
num2 = 20
calculator(num1, num2)