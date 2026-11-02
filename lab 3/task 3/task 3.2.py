mass = []
s = 15
print(f"Заполнение массива из {s} элементов:")
x = 0
while x < s:
    f_in = True
    while f_in:
        try:
            val = int(input(f"Введите целое число {x + 1} из 15: "))
            mass.append(val)
            f_in = False
        except ValueError:
            print("Неверно введено число. Введите целое число.")
    x += 1
mass2 = mass.copy()
f_process = True
x2 = 0
while f_process:
    if mass2[x2] < 10:
        mass2[x2] = 0
    elif mass2[x2] > 20:
        mass2[x2] = 1
    x2 += 1
    if x2 == s:
        f_process = False
print("Первоначальный массив:", *mass)
print("Преобразованный массив:", *mass2)