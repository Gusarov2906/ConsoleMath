from MathStr import My_math
from MathStr import My_converting
from MathStr import Database


def main():
    print(
        "ConsoleMATH by Andrey Gusarov\nIf you want to see all commands, write 'help'\n"
        "If you want to finish, write 'exit'")
    database = Database.Database()
    database.load_from_file()
    while True:
        string = input(">>> ")
        if string == 'exit':
            break
        elif string == 'help':
            print(
                "Commands:\nhelp - All commands\nhistory - Show 10 recent expressions\n"
                "clear - Clear all history\nexit - Finish work")
            continue
        elif string == 'history':
            database.print()
            continue
        elif string == "clear":
            database.clear()
            continue
        database.add_expression(string)
        string = My_math.solve(string)
        if string is not None:
            string = My_converting.convert_to_str(string)
            print(f'Result: {string} ')
        database.add_result(string)
    database.save_to_file()


"""    mas = convert_to_mas(string)
    # print(mas)
    mas = solve(mas)
    string = convert_to_str(mas)
    print(f'>>> {string}')
    return 0
"""

main()
