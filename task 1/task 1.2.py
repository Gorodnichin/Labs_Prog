f = True
A = 0.0
while f:
    try:
        A = float(input('Введите число A: '))
        if A > 0:
            f = False
        else:
            print("Число A должно быть больше 0")
    except ValueError:
        print("Неверно введено число. Пожалуйста, введите вещественное число.")
K = 0
q = 0.0
while q + 1 / (K + 1) < A:
    K = K + 1
    q = q + 1 / K
print('Наибольшее K:', K)
print('Сумма: ', q)
