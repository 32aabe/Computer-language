while True:
    print("Hello, I'm caculator. You can choose one option among them. Please select one.")
    print("1. add   2. subtract   3. divide    4. multiply    5. finish")
    answer = input()

    print("Please enter the number you want to calculate.")
    a = float(input('first number: '))
    b = float(input('second number: '))

    if answer == '1' :
        print(a, '+', b, '=',  a + b)
    elif answer == '2' :
        print(a, '-', b, '=', a + b)
    elif answer == '3' :
        print(a, '/', b, '=', a / b)
    elif answer == '4' :
        print(a, '*', b, '=', a * b)
    elif answer == '5' :
        print('finished')
        break