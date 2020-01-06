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
    # print(str_value)
    return str_value, n


# bool функция на проверку на арифметический символ
def is_arithmetic_sign(char):
    if char == "+" or char == "-" or char == "/" or char == "*" or char == "^":
        return True
    return False


# bool функция на проверку на символ скобки символ
def is_parentheses_sign(char):
    if char == "a" or char == "e" or char == f'a{int}' or char == "en":
        return True
    return False


# bool функция на проверку на символ открывающейся скобки символ
def is_parentheses_open_sign(char):
    if char == "a" or char == f'a{int}':
        return True
    return False


# bool функция на проверку на символ закрывающийся скобки символ
def is_parentheses_close_sign(char):
    if char == "a" or char == f'a{int}':
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
    is_negative = False
    is_number = False
    is_parentheses = False
    count_open_parentheses = 0
    count_closed_parentheses = 0
    for i in range(len(str_value)):
        if is_parentheses:
            is_parentheses = False
            continue
        if i == 0:
            if str_value[i] == "-":
                is_negative = True
        else:
            if is_arithmetic_sign(str_value[i - 1]) or is_indentation(str_value[i - 1]):
                if str_value[i] == "-":
                    is_negative = True
        if str_value[i].isdigit() or str_value[i] == '.':
            val += str_value[i]
            is_number = True
            continue
        if str_value[i] == '-':
            if is_negative:
                val += str_value[i]
                is_number = True
                is_negative = False
                continue
        if is_number:
            mas.append(val)
            is_number = False
        if is_arithmetic_sign(str_value[i]):
            mas.append(str_value[i])
        elif i < len(str_value) - 1 and is_parentheses_sign(str_value[i]):
            if is_parentheses_open_sign(str_value[i]):
                count_open_parentheses += 1
                mas.append(str_value[i] + str_value[i + 1])
                is_parentheses = True
            else:
                count_closed_parentheses += 1
                mas.append(str_value[i] + str_value[i + 1])
                is_parentheses = True
        elif is_indentation(str_value[i]):
            continue
        else:
            print(f'Invalid symbol: {str_value[i]}')
            exit()
        val = ""
    if is_number:
        mas.append(val)
    try:
        if count_closed_parentheses != count_open_parentheses:
            raise Exception("Error with parentheses!")
    except Exception as e:
        print(e)
        exit()
    return mas


# функция проверяет на наличие скобок
def has_parentheses(str_value):
    for i in range(len(str_value)):
        if is_parentheses_sign(str_value[i]):
            return True
    return False


# функция собирает из массива строку
def convert_to_str(mas):
    string = ""
    for i in range(len(mas)):
        string += str(mas[i])
    return string
