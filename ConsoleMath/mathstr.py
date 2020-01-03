# Умножение
def my_multiply(x, y):
    try:
        x = int(x)
        y = int(y)
        res = x * y
    except Exception as e:
        print("Multiply error!")
        print(e)
        res = 0
    return res


# Сложение
def my_addition(x, y):
    try:
        x = int(x)
        y = int(y)
        res = x + y
    except Exception as e:
        print("Addition error!")
        print(e)
        res = 0
    return res


# Вычитание
def my_subtraction(x, y):
    try:
        x = int(x)
        y = int(y)
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
        x = int(x)
        y = int(y)
        res = x ** y
    except Exception as e:
        print("Exponentiation error!")
        print(e)
        res = 0
    return res


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
                mas = convert_to_str(mas)
                mas = convert_to_mas(mas)
                print(mas)
                break
            flag1 = False
        if flag1 is False:
            break


def my_division_for_mas(mas):
    flag1 = False
    while True:
        for i in range(len(mas)):
            if mas[i] == "/":
                flag1 = True
                mas[i] = my_division(mas[i - 1], mas[i + 1])
                mas[i - 1] = " "
                mas[i + 1] = mas[i]
                mas[i] = " "
                mas = convert_to_str(mas)
                mas = convert_to_mas(mas)
                print(mas)
                break
            flag1 = False
        if flag1 is False:
            break


def my_multiply_for_mas(mas):
    flag1 = False
    while True:
        for i in range(len(mas)):
            if mas[i] == "*":
                flag1 = True
                mas[i] = my_multiply(mas[i - 1], mas[i + 1])
                mas[i - 1] = " "
                mas[i + 1] = mas[i]
                mas[i] = " "
                mas = convert_to_str(mas)
                mas = convert_to_mas(mas)
                print(mas)
                break
            flag1 = False
        if flag1 is False:
            break


def my_addition_for_mas(mas):
    flag1 = False
    while True:
        for i in range(len(mas)):
            if mas[i] == "+":
                flag1 = True
                mas[i] = my_addition(mas[i - 1], mas[i + 1])
                mas[i - 1] = " "
                mas[i + 1] = mas[i]
                mas[i] = " "
                mas = convert_to_str(mas)
                mas = convert_to_mas(mas)
                print(mas)
                break
            flag1 = False
        if flag1 is False:
            break


def my_subtraction_for_mas(mas):
    flag1 = False
    while True:
        for i in range(len(mas)):
            if mas[i] == "^":
                flag1 = True
                mas[i] = my_subtraction(mas[i - 1], mas[i + 1])
                mas[i - 1] = " "
                mas[i + 1] = mas[i]
                mas[i] = " "
                mas = convert_to_str(mas)
                mas = convert_to_mas(mas)
                print(mas)
                break
            flag1 = False
        if flag1 is False:
            break


"""
# Преобразование строки с учетом скобок
def convert_str(str_value):
    n = 0
    mas = []
    for i in range(len(str_value)):
        mas.append(str_value[i])
    str_value = ""
    for i in range(len(mas)):
        if mas[i] == "(":
            n += 1
            mas[i] = f"'{n}'"
        if mas[i] == ")":
            mas[i] = f"'end'"
        str_value += mas[i]
    return str_value, n
"""


def is_arithmetic_sign(char):
    if char == "+" or char == "-" or char == "/" or char == "*" or char == "^":
        return True
    return False


def is_indentation(char):
    if char == " " or char == "\n" or char == "\t":
        return True
    return False


def convert_to_mas(str_value):
    mas = []
    val = ""
    flag = False
    for i in range(len(str_value)):
        if str_value[i].isdigit() or str_value[i] == '.':
            val += str_value[i]
            flag = True
            continue
        if flag:
            mas.append(val)
            flag = False
        if is_arithmetic_sign(str_value[i]):
            mas.append(str_value[i])
        elif is_indentation(str_value[i]):
            continue
        else:
            print("Invalid symbol")
            return None
        val = ""
    if flag:
        mas.append(val)
    return mas


def convert_to_str(mas):
    string = ""
    for i in range(len(mas)):
        string += str(mas[i])
    return string

"""
def solve(mas):
    flag1 = False
    while True:
        for i in range(len(mas)):
            if mas[i] == "^":
                flag1 = True
                mas[i] = my_exponentiation(mas[i - 1], mas[i + 1])
                mas[i - 1] = " "
                mas[i + 1] = mas[i]
                mas[i] = " "
                mas = convert_to_str(mas)
                mas = convert_to_mas(mas)
                print(mas)
                break
            flag1 = False
        if flag1 is False:
            break
"""

def main():
    string = input("Write str: ")
    mas = convert_to_mas(string)
    print(mas)
    my_division_for_mas(mas)
    return 0


main()
