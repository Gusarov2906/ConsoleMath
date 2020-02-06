string = input("Write str: ")
mas = []
for i in range(len(string)):
    mas.append(string[i])
counter = 0
counte_not_closed = 0
counter_dop = 0
for i in range(len(mas)):
    if mas[i] == "(":
        counter += 1
        counter_dop += 1
        counte_not_closed += 1
        mas[i] = counter
    if mas[i] == ")":
        mas[i] = counter_dop
        counte_not_closed -= 1
        if counte_not_closed > 0:
            counter_dop -= 1
        else:
            counter_dop = counter

print(mas)