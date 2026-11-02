s = 0
x = 20
i = 0
while i < x:
    f = True
    while f:
        try:
            x = int(input(f'Введите оценку {i + 1} из {x}: '))
            if 1 <= x <= 5:
                s += x
                f = False
            else:
                print("Оценка должна быть в диапазоне от 1 до 5")
        except ValueError:
            print("Неверно введено число. Введите целое число.")
    i += 1
q = s / x
print('Средняя оценка:', q)
