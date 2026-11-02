import math
print ("Меню выбора материала")
print("1-Древесина")
print("2-Керамика")
print("3-Зерно")
f1=True
while(f1):
    try:
        choice=int(input("Выберите число 1-3:"))
        match choice:
            case 1:
                material="Древесина"
                k=0.008
                f1=False
            case 2:
                material="Керамика"
                k=0.004
                f1=False
            case 3:
                material="Зерно"
                k=0.012
                f1=False
            case _:
                print("Неверно выбрано число")
    except ValueError:
        print("Введите целое число")
print("Введите массу m")
f2=True
while(f2):
    try:
        m=float(input(("Введите число от 1 до 5000:")))
        if 1<=m<=5000:
         f2=False
        else: print("Масса должна быть в диапазоне от 1 до 5000")
    except ValueError:
        print("Неверно выбрано число")
print("Введите начальную влажность w1:")
f3=True
while(f3):
    try:
        w1=int(input("Введите проценты от 5 до 60:"))
        if 5<=w1<=60:
         f3=False
        else: print("Проценты должны бать от 5 до 60")
    except ValueError:
        print("Неверно выбрано число")
print("Введите конечную влажность w2:")
f4=True
while(f4):
    try:
        w2=int(input("Введите число от 0 до 30:"))
        if 0<=w2<=30 and w2<w1:
            f4 = False
        else:
            print("Конечная влажность должна быть от 0 до 30 и меньше начальной (w2 < w1)")
    except ValueError:
        print("Неверно выбрано число")
print("Введите температуру сушильного агента t:")
f5 = True
while f5:
    try:
        T = float(input("Введите число от 40 до 250: "))
        if 40 <= T <= 250:
            f5 = False
        else:
            print("Температура должна быть в диапазоне от 40 до 250")
    except ValueError:
        print("Неверно выбрано число")
m_w = m * (w1 - w2) / (100 - w2)
if w2 == 0:
    t = float('inf')
else:
    t = (1 / k) * math.log(w1 / w2)
if t < 2:
    drying_class = "быстрая сушка"
elif 2 <= t <= 12:
    drying_class = "нормальная"
else:
    drying_class = "длительная"
print("Материал:", material)
print("Масса удаляемой воды (кг):", m_w)
print("Время сушки (ч):", t)
print("Класс сушки:", drying_class)