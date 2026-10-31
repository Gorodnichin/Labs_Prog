A=float(input('Введите число A: '))
K=0
q=0
while q+1/(K+1)<A:
    K=K+1
    q=q+1/K
print ('Наибольшее K:', K)
print ('Сумма: ', q)