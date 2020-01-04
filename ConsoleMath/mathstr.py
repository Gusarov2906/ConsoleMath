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
        mas = convert_to_str(mas)
        mas = convert_to_mas(mas)
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
        mas = convert_to_str(mas)
        mas = convert_to_mas(mas)
        if flag1 is False:
            break
    return mas


"""
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
                # print(mas)
                continue
            flag1 = False
        mas = convert_to_str(mas)
        mas = convert_to_mas(mas)
        if flag1 is False:
            break
    return mas
"""


# функция всех сложения и вычитания слева на права по порядку
def my_addition_and_subtraction_for_mas(mas):
    flag1 = False
    while True:
        for i in range(len(mas)):
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
        mas = convert_to_str(mas)
        mas = convert_to_mas(mas)
        if flag1 is False:
            break
    return mas


"""
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
                # print(mas)
                continue
            flag1 = False
        mas = convert_to_str(mas)
        mas = convert_to_mas(mas)
        if flag1 is False:
            break
    return mas
"""
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


# bool функция на проверку на арифметический символ
def is_arithmetic_sign(char):
    if char == "+" or char == "-" or char == "/" or char == "*" or char == "^":
        return True
    return False


# bool функция на проверку пробела, табуляции и переноса строки в символе
def is_indentation(char):
    if char == " " or char == "\n" or char == "\t":
        return True
    return False


# функция делает из строки массив, в котором отдельно лежат по исходному порядку в строке числа и арифметические знаки
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


# функция собирает из массива строку
def convert_to_str(mas):
    string = ""
    for i in range(len(mas)):
        string += str(mas[i])
    return string


# Функия, проводящая вычисления коненчного ответа, вызывающая в нужном порядке арифметические действия
def solve(mas):
    mas = my_exponentiation_for_mas(mas)
    mas = my_division_and_multiply_for_mas(mas)
    mas = my_addition_and_subtraction_for_mas(mas)
    # print(type(mas[0]))
    #  Проверка на возможность преобразования в int и если возможно, то преобразует, иначе оставляет float
    if len(mas) == 1:
        try:
            mas[0] = float(mas[0])
            if mas[0] == int(mas[0]):
                mas[0] = int(mas[0])
        except Exception as e:
            mas[0] = float(mas[0])
            print(e)
    elif len(mas) == 2:
        try:
            mas[1] = float(mas[1])
            if mas[1] == int(mas[1]):
                mas[1] = int(mas[1])
        except Exception as e:
            mas[1] = float(mas[1])
            print(e)

    # print(mas)
    return mas


def main():
    string = input(">>> ")
    mas = convert_to_mas(string)
    # print(mas)
    mas = solve(mas)
    string = convert_to_str(mas)
    print(f'>>> {string}')
    return 0


main()
