from MathStr import My_arithmetic
from MathStr import My_converting


#  Проверка на возможность преобразования в int и если возможно, то преобразует, иначе оставляет float
def check_type_output(mas):
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
    return mas


# Функия, проводящая вычисления коненчного ответа, вызывающая в нужном порядке арифметические действия
def solve(mas):
    n1 = 0
    n2 = 0
    has_parentheses = False
    mas, n = My_converting.convert_str_parentheses(mas)
    mas = My_converting.convert_to_mas(mas)
    has_parentheses = My_converting.has_parentheses(mas)
    while n >= 0:
        for i in range(0, len(mas)):
            if mas[i] == "a" + str(n):
                n1 = i
                break
        else:
            n1 = 0
        for i in range(n1, len(mas)):
            if mas[i] == "en":
                n2 = i
                break
        else:
            n2 = len(mas)

        # print(n1, n2)
        if has_parentheses:
            new_mas = mas[n1:n2]
            n -= 1
            new_mas.pop(0)
            new_mas = My_arithmetic.solve_without_parentheses(new_mas)
            for i in range(n1, n2 + 1):
                mas.pop(n1)
            mas.insert(n1, new_mas[0])
            if len(new_mas) == 2:
                mas.insert(n1 + 1, new_mas[1])
            has_parentheses = My_converting.has_parentheses(mas)
        else:
            new_mas = mas
            n -= 1
            new_mas = My_arithmetic.solve_without_parentheses(new_mas)
            mas = new_mas
    # print(type(mas[0]))
    #  Проверка на возможность преобразования в int и если возможно, то преобразует, иначе оставляет float
    mas = check_type_output(mas)
    # print(mas)
    return mas


def main():
    string = input(">>> ")
    string = solve(string)
    string = My_converting.convert_to_str(string)
    print(string)


"""    mas = convert_to_mas(string)
    # print(mas)
    mas = solve(mas)
    string = convert_to_str(mas)
    print(f'>>> {string}')
    return 0
"""

main()
