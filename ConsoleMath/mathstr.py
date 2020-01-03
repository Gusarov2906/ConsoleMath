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
        x = int(x)
        y = int(y)
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


def convert_to_mas(str_value):
    mas = []
    val = ""
    flag = False
    for i in range(len(str_value)):
        if str_value[i].isdigit():
            val += str_value[i]
            flag = True
            continue
        if flag:
            mas.append(val)
            flag = False
        mas.append(str_value[i])
        val = ""
    if flag:
        mas.append(val)
    return mas


"""
def solve(mas):
    for i in range(len(mas)):
        if mas[i] == "^":"""


def main():
    string = input("Write str: ")
    mas = convert_to_mas(string)
    print(mas)


main()
