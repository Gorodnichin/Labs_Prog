list = []
print("Определите размер списка")
f_size = True
s = 0
while f_size:
    try:
        s = int(input("Сколько элементов вы хотите ввести? (минимум 1): "))
        if s >= 1:
            f_size = False
        else:
            print("Количество элементов должно быть больше 0")
    except ValueError:
        print("Неверно введено число. Введите целое число.")
print(f"Заполнение списка из {s} элементов:")
x = 0
while x < s:
    f_input = True
    while f_input:
        try:
            val = int(input(f"Введите целое число для элемента {x + 1}: "))
            list.append(val)
            f_input = False
        except ValueError:
            print("Неверно введено число. Пожалуйста, введите целое число.")
    x += 1
duplicate_found = False
f_check = True
i = 0
while f_check:
    if i < len(list):
        item = list[i]
        if list.count(item) > 1:
            print("Найден повторяющийся элемент:", item)
            duplicate_found = True
            f_check = False   
        i += 1
    else:
        f_check = False
if not duplicate_found:
    print("Повторяющиеся элементы отсутствуют.")