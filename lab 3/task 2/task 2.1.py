f_input = True
s = ''
while f:
    try:
        s = input('Введите строку: ') 
        if len(s.strip()) > 0:
            f = False
        else:
            print("Строка не должна быть пустой. Пожалуйста, введите текст.")     
    except ValueError:
        print("Произошла ошибка при вводе текста.")
q = ''
for i in range(len(s)):
    if i == 0 or s[i-1] == ' ':
        q = q + s[i].upper()
    else:
        q = q + s[i].lower()    
print(q)
