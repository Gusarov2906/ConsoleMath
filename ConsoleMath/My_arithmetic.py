from MathStr import My_converting


# Умножение
def my_multiply(x, y):
    try:
        x = float(x)
        y = float(y)
        res = x * y
    except Exception as e:
        print("Multiply error!")
        print(e)
        res = 0
    return res


# Сложение
def my_addition(x, y):
    try:
        x = float(x)
        y = float(y)
        res = x + y
    except Exception as e:
        print("Addition error!")
        print(e)
        res = 0
    return res


# Вычитание
def my_subtraction(x, y):
    try:
        x = float(x)
        y = float(y)
        res = x - y
    except Exception as e:
        print("Subtraction error!")
        print(e)
        res = 0
    return res


# Деление
def my_division(x, y):
    try:
        x = float(x)
        y = float(y)
        res = x / y
    except Exception as e:
        print("Division error!")
        print(e)
        res = 0
    return res


# Возведение в степень
def my_exponentiation(x, y):
    try:
        x = float(x)
        y = float(y)
        res = x ** y
    except Exception as e:
        print("Exponentiation error!")
        print(e)
        res = 0
    return res


# функция всех возведений в степень слева на права по порядку
def my_exponentiation_for_mas(mas):
    flag1 = False
    while True:
        for i in range(len(mas)):
            if mas[i] == "^":
                flag1 = True
                mas[i] = my_exponentiation(mas[i - 1], mas[i + 1])
                mas[i - 1] = " "
                mas[i + 1] = mas[i]
                mas[i] = " "
                # print(mas)
                continue
            flag1 = False
        mas = My_converting.convert_to_str(mas)
        mas = My_converting.convert_to_mas(mas)
        if flag1 is False:
            break
    return mas


# функция всех делений и умножений слева на права по порядку
def my_division_and_multiply_for_mas(mas):
    flag1 = False
    while True:
        for i in range(len(mas)):
            if mas[i] == "/":
                flag1 = True
                mas[i] = my_division(mas[i - 1], mas[i + 1])
                mas[i - 1] = " "
                mas[i + 1] = mas[i]
                mas[i] = " "
                # print(mas)
                continue
            if mas[i] == "*":
                flag1 = True
                mas[i] = my_multiply(mas[i - 1], mas[i + 1])
                mas[i - 1] = " "
                mas[i + 1] = mas[i]
                mas[i] = " "
                # print(mas)
                continue
            flag1 = False
        mas = My_converting.convert_to_str(mas)
        mas = My_converting.convert_to_mas(mas)
        if flag1 is False:
            break
    return mas


# функция всех сложения и вычитания слева на права по порядку
def my_addition_and_subtraction_for_mas(mas):
    flag1 = False
    while True:
        for i in range(len(mas)):
            if i > 0:
                if mas[i] == "+":
                    flag1 = True
                    mas[i] = my_addition(mas[i - 1], mas[i + 1])
                    mas[i - 1] = " "
                    mas[i + 1] = mas[i]
                    mas[i] = " "
                    # print(mas)
                    continue
                if mas[i] == "-":
                    flag1 = True
                    mas[i] = my_subtraction(mas[i - 1], mas[i + 1])
                    mas[i - 1] = " "
                    mas[i + 1] = mas[i]
                    mas[i] = " "
                    # print(mas)
                    continue
            flag1 = False
        mas = My_converting.convert_to_str(mas)
        mas = My_converting.convert_to_mas(mas)
        if flag1 is False:
            break
    return mas


def solve_without_parentheses(mas):
    mas = my_exponentiation_for_mas(mas)
    mas = my_division_and_multiply_for_mas(mas)
    mas = my_addition_and_subtraction_for_mas(mas)
    return mas
