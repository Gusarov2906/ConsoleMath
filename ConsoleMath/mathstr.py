from MathStr import My_math
from MathStr import My_converting


def main():
    print("ConsoleMATH by Andrey Gusarov\nIf you want to finish, write 'exit'")
    while True:
        string = input(">>> ")
        if string == 'exit':
            break
        string = My_math.solve(string)
        if string is not None:
            string = My_converting.convert_to_str(string)
            print(f'Result: {string} ')



"""    mas = convert_to_mas(string)
    # print(mas)
    mas = solve(mas)
    string = convert_to_str(mas)
    print(f'>>> {string}')
    return 0
"""

main()
