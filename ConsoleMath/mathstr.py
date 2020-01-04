from MathStr import My_arithmetic


# Преобразование строки с учетом скобок
def convert_str_parentheses(str_value):
    n = 0
    mas = []
    for i in range(len(str_value)):
        mas.append(str_value[i])
    str_value = ""
    for i in range(len(mas)):
        if mas[i] == "(":
            n += 1
            mas[i] = f"a{n}"
        if mas[i] == ")":
            mas[i] = f"en"
        str_value += mas[i]
    print(str_value)
    return str_value, n


# bool функция на проверку на арифметический символ
def is_arithmetic_sign(char):
    if char == "+" or char == "-" or char == "/" or char == "*" or char == "^":
        return True
    return False


# bool функция на проверку на арифметический символ
def is_parentheses_sign(char):
    if char == "a" or char == "e":
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
    flag2 = False
    for i in range(len(str_value)):
        if flag2:
            flag2 = False
            continue
        if str_value[i].isdigit() or str_value[i] == '.':
            val += str_value[i]
            flag = True
            continue
        if flag:
            mas.append(val)
            flag = False
        if is_arithmetic_sign(str_value[i]):
            mas.append(str_value[i])
        elif i < len(str_value) - 1:
            if is_parentheses_sign(str_value[i]):
                mas.append(str_value[i] + str_value[i + 1])
                flag2 =True
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
    n1 = 0
    n2 = 0
    mas, n = convert_str_parentheses(mas)
    mas = convert_to_mas(mas)
    while n > 0:
        for i in range(0, len(mas)):
            if mas[i] == "a" + str(n):
                n1 = i
                break
        for i in range(n1, len(mas)):
            if mas[i] == "en":
                n2 = i
                break

        print(n1, n2)
        new_mas = mas[n1+1:n2]
        n -= 1
        print(new_mas)
        # new_mas = solve(new_mas)
        n1 -= 1
    mas = My_arithmetic.my_exponentiation_for_mas(mas)
    mas = My_arithmetic.my_division_and_multiply_for_mas(mas)
    mas = My_arithmetic.my_addition_and_subtraction_for_mas(mas)
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

    print(mas)
    return mas


def main():
    string = input(">>> ")
    solve(string)


"""    mas = convert_to_mas(string)
    # print(mas)
    mas = solve(mas)
    string = convert_to_str(mas)
    print(f'>>> {string}')
    return 0
"""

main()
